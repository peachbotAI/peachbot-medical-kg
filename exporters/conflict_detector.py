def detect_conflicts(rules):
    """
    Detect conflicting rules based on overlapping inputs.
    """

    conflicts = []

    for i in range(len(rules)):
        for j in range(i + 1, len(rules)):

            r1 = rules[i].ku
            r2 = rules[j].ku

            # Compare symptoms overlap
            overlap = set(r1.inputs.symptoms) & set(r2.inputs.symptoms)

            if not overlap:
                continue

            # Check if signals differ
            if r1.signal.id != r2.signal.id:

                conflicts.append({
                    "rule_1": r1.signal.id,
                    "rule_2": r2.signal.id,
                    "overlap_symptoms": list(overlap),
                    "issue": "Conflicting signals for similar inputs"
                })

    return conflicts