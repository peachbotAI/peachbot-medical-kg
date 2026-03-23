def detect_conflicts(rules):
    """
    Detect conflicting rules based on overlapping inputs.

    Improved logic:
    - Requires significant overlap (>= 2 symptoms)
    - Must belong to same system
    - Avoids flagging hierarchical refinement as conflict
    """

    conflicts = []

    for i in range(len(rules)):
        for j in range(i + 1, len(rules)):

            r1 = rules[i].ku
            r2 = rules[j].ku

            # Overlapping symptoms
            overlap = set(r1.inputs.symptoms) & set(r2.inputs.symptoms)

            # Require meaningful overlap
            if len(overlap) < 2:
                continue

            # Same system (important for clinical relevance)
            if r1.context.system != r2.context.system:
                continue

            # Different signals
            if r1.signal.id != r2.signal.id:

                # Heuristic: check specificity (more inputs = more specific)
                r1_specificity = len(r1.inputs.symptoms) + len(r1.inputs.signs) + len(r1.inputs.investigations)
                r2_specificity = len(r2.inputs.symptoms) + len(r2.inputs.signs) + len(r2.inputs.investigations)

                # If one is clearly more specific → NOT a conflict (hierarchical refinement)
                if abs(r1_specificity - r2_specificity) >= 2:
                    continue

                # Otherwise → potential conflict
                conflicts.append({
                    "rule_1": r1.signal.id,
                    "rule_2": r2.signal.id,
                    "overlap_symptoms": list(overlap),
                    "issue": "Potential conflicting signals with similar specificity"
                })

    return conflicts