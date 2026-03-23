import yaml
from configs.config_loader import load_config


def load_scoring_config():
    with open("configs/scoring.yaml", "r") as f:
        return yaml.safe_load(f)


def score_rule(rule, config):
    ku = rule.ku

    score = 0

    # Base weight
    score += ku.meta.weight * config["weights"]["base_weight_multiplier"]

    # Confidence contribution
    score += ku.meta.confidence * config["weights"]["confidence_multiplier"]

    # Boosts

    # Severity boost
    if ku.context.severity.value == "high":
        score *= config["boosts"]["high_severity_bonus"]

    # Multi-symptom boost
    if len(ku.inputs.symptoms) > 2:
        score *= config["boosts"]["multi_symptom_bonus"]

    # Investigation boost
    if ku.inputs.investigations:
        score *= config["boosts"]["investigation_bonus"]

    # Penalty

    if ku.meta.confidence < 0.5:
        score *= config["penalties"]["low_confidence_penalty"]

    return score


def rank_rules(rules):
    config = load_scoring_config()

    scored = []

    for rule in rules:
        s = score_rule(rule, config)

        scored.append({
            "signal": rule.ku.signal.id,
            "score": round(s, 3),
            "confidence": rule.ku.meta.confidence
        })

    # Sort descending
    scored.sort(key=lambda x: x["score"], reverse=True)

    return scored