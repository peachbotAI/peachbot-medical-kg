def generate_explanations(safe_outputs, rules):
    """
    Convert structured outputs into human-readable explanations.
    """

    explanations = []

    for output in safe_outputs:
        signal_id = output["signal"]

        # 🔹 Get supporting rules
        related_rules = [
            r for r in rules if r.ku.signal.id == signal_id
        ]

        # 🔹 Build explanation parts
        symptoms = set()
        notes = []
        evidence_sources = set()

        for rule in related_rules:
            symptoms.update(rule.ku.inputs.symptoms)
            notes.append(rule.ku.meta.explanation)

            for e in rule.ku.evidence:
                evidence_sources.add(e.source)

        # 🔹 Compose explanation
        explanation_text = (
            f"{output['risk_level'].capitalize()}-risk pattern detected. "
            f"Observed features include {', '.join(symptoms)}. "
            f"{notes[0]}."
        )

        explanations.append({
            "signal": signal_id,
            "explanation": explanation_text,
            "risk_level": output["risk_level"],
            "urgency": output["urgency"],
            "recommended_action": output["recommended_action"],
            "evidence_sources": list(evidence_sources)
        })

    return explanations