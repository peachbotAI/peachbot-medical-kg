from schema.clinical_schema import ClinicalKnowledgeUnit
from schema.validators import validate_knowledge_unit


class ClinicalRule:
    """
    Wraps a ClinicalKnowledgeUnit and converts it
    into PeachBot Core-compatible format.
    """

    def __init__(self, ku: ClinicalKnowledgeUnit):
        validate_knowledge_unit(ku)  # 🔒 enforce validation
        self.ku = ku

    def to_core_format(self) -> dict:
        """
        Convert Knowledge Unit → PeachBot Core JSON
        """

        return {
            "conditions": {
                "symptoms": self.ku.inputs.symptoms,
                "signs": self.ku.inputs.signs,
                "investigations": self.ku.inputs.investigations,
                "severity": self.ku.context.severity.value,
                "duration": self.ku.context.duration.value,
                "system": self.ku.context.system.value,
            },
            "signal": {
                "id": self.ku.signal.id,
                "priority": self.ku.signal.priority,
                "type": self.ku.signal.type,
            },
            "tags": self.ku.meta.tags,
            "weight": self.ku.meta.weight,
            "confidence": self.ku.meta.confidence,
            "note": self.ku.meta.explanation,
            "evidence": [
                {
                    "source": e.source,
                    "concept": e.concept,
                    "level": e.level.value,
                    "strength": e.strength.value,
                    "reference": e.reference,
                }
                for e in self.ku.evidence
            ],
        }