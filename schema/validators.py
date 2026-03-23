from schema.clinical_schema import ClinicalKnowledgeUnit


class ValidationError(Exception):
    pass


def validate_knowledge_unit(ku: ClinicalKnowledgeUnit):

    # ✅ Evidence must exist
    if not ku.evidence or len(ku.evidence) == 0:
        raise ValidationError("Knowledge Unit must include at least one evidence source.")

    # ✅ Inputs must not be empty
    if not (ku.inputs.symptoms or ku.inputs.signs or ku.inputs.investigations):
        raise ValidationError("At least one input (symptom/sign/investigation) is required.")

    # ✅ Confidence range
    if not (0.0 <= ku.meta.confidence <= 1.0):
        raise ValidationError("Confidence must be between 0 and 1.")

    # ✅ Weight sanity
    if ku.meta.weight < 1:
        raise ValidationError("Weight must be >= 1.")

    # ✅ Explanation required
    if not ku.meta.explanation:
        raise ValidationError("Explanation is required for clinical traceability.")

    return True