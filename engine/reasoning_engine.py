import yaml
from collections import defaultdict

from exporters.scoring_engine import score_rule, load_scoring_config


def load_reasoning_config():
    with open("configs/reasoning.yaml", "r") as f:
        return yaml.safe_load(f)


def apply_dominance(results):
    """
    Suppress weaker/general signals when stronger ones exist.

    Logic:
    - If another signal has higher score AND >= confidence → suppress weaker
    - Prevents redundant outputs (hierarchical refinement case)
    """

    final = []

    for i, r1 in enumerate(results):
        dominated = False

        for j, r2 in enumerate(results):
            if i == j:
                continue

            # Stronger signal dominates weaker one
            if (
                r2["score"] > r1["score"] and
                r2["confidence"] >= r1["confidence"]
            ):
                dominated = True
                break

        if not dominated:
            final.append(r1)

    return final


def run_reasoning(rules):
    """
    Main reasoning pipeline:
    - score rules
    - filter low-quality signals
    - aggregate signals
    - apply dominance (clinical suppression)
    - produce final ranked outputs
    """

    reasoning_config = load_reasoning_config()
    scoring_config = load_scoring_config()

    # Step 1: Score rules
    scored_rules = []

    for rule in rules:
        score = score_rule(rule, scoring_config)
        scored_rules.append((rule, score))

    # Step 2: Filter by minimum score
    min_score = reasoning_config["thresholds"]["minimum_score"]
    scored_rules = [(r, s) for r, s in scored_rules if s >= min_score]

    # Step 3: Sort by score
    scored_rules.sort(key=lambda x: x[1], reverse=True)

    # Step 4: Aggregate signals
    aggregated = defaultdict(lambda: {
        "score": 0,
        "count": 0,
        "confidence": 0,
        "rules": []
    })

    for rule, score in scored_rules:
        signal_id = rule.ku.signal.id

        aggregated[signal_id]["score"] += score
        aggregated[signal_id]["count"] += 1
        aggregated[signal_id]["confidence"] += rule.ku.meta.confidence
        aggregated[signal_id]["rules"].append(rule)

    # Step 5: Normalize + prepare output
    results = []

    for signal_id, data in aggregated.items():
        avg_conf = data["confidence"] / data["count"]

        results.append({
            "signal": signal_id,
            "score": round(data["score"], 3),
            "confidence": round(avg_conf, 3),
            "supporting_rules": data["count"]
        })

    # Step 6: Sort final signals
    results.sort(key=lambda x: x["score"], reverse=True)

    # Step 7: Top-K filtering
    top_k = reasoning_config["aggregation"]["top_k_signals"]
    results = results[:top_k]

    # Step 8: Apply dominance (NEW)
    # results = apply_dominance(results)
    if reasoning_config.get("dominance", {}).get("enabled", True):
        results = apply_dominance(results)

    return results