import json
import os

from exporters.conflict_detector import detect_conflicts
from exporters.scoring_engine import rank_rules


def generate_report(rules, output_dir):
    """
    Generate a validation and analysis report for all rules.

    Includes:
    - Rule statistics
    - Evidence checks
    - Conflict detection
    - Scoring & ranking
    """

    report = {
        "summary": {
            "total_rules": 0,
            "high_confidence_rules": 0,
            "missing_evidence": 0
        },
        "conflicts": [],
        "ranking": [],
        "errors": []
    }

    # 🔹 Summary metrics
    report["summary"]["total_rules"] = len(rules)

    for rule in rules:
        ku = rule.ku

        # High confidence tracking
        if ku.meta.confidence >= 0.8:
            report["summary"]["high_confidence_rules"] += 1

        # Evidence check
        if not ku.evidence:
            report["summary"]["missing_evidence"] += 1
            report["errors"].append({
                "signal": ku.signal.id,
                "issue": "Missing evidence"
            })

        # Confidence sanity check
        if not (0.0 <= ku.meta.confidence <= 1.0):
            report["errors"].append({
                "signal": ku.signal.id,
                "issue": "Invalid confidence value"
            })

    # Conflict detection
    try:
        conflicts = detect_conflicts(rules)
        report["conflicts"] = conflicts
    except Exception as e:
        report["errors"].append({
            "stage": "conflict_detection",
            "issue": str(e)
        })

    # Scoring & ranking
    try:
        ranking = rank_rules(rules)
        report["ranking"] = ranking
    except Exception as e:
        report["errors"].append({
            "stage": "scoring",
            "issue": str(e)
        })

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    report_path = os.path.join(output_dir, "report.json")

    # Write report
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    print(f"[✓] Validation report generated → {report_path}")