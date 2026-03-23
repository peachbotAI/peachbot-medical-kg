import yaml


def load_safety_config():
    with open("configs/safety.yaml", "r") as f:
        return yaml.safe_load(f)


def evaluate_safety(final_signals, rules):
    """
    Assign risk level, urgency, and actions based on:
    - red flag symptoms
    - severity context
    """

    config = load_safety_config()

    enriched_outputs = []

    for signal in final_signals:

        signal_id = signal["signal"]

        # 🔹 Collect supporting rules
        related_rules = [
            r for r in rules if r.ku.signal.id == signal_id
        ]

        detected_red_flags = set()
        max_risk = config["defaults"]["risk"]
        urgency = config["defaults"]["urgency"]
        action = config["defaults"]["action"]

        # 🔹 Check red flags
        for rule in related_rules:
            symptoms = rule.ku.inputs.symptoms

            for symptom in symptoms:
                if symptom in config["red_flags"]:
                    detected_red_flags.add(symptom)

                    rf = config["red_flags"][symptom]

                    max_risk = rf["risk"]
                    urgency = rf["urgency"]
                    action = rf["action"]

        # 🔹 If no red flag, use severity-based rule
        if not detected_red_flags:
            for rule in related_rules:
                severity = rule.ku.context.severity.value

                if severity == "high":
                    max_risk = config["risk_rules"]["high_severity"]["risk"]
                    urgency = config["risk_rules"]["high_severity"]["urgency"]

                elif severity == "moderate":
                    max_risk = config["risk_rules"]["moderate_severity"]["risk"]
                    urgency = config["risk_rules"]["moderate_severity"]["urgency"]

        enriched_outputs.append({
            **signal,
            "risk_level": max_risk,
            "urgency": urgency,
            "recommended_action": action,
            "red_flags": list(detected_red_flags)
        })

    return enriched_outputs