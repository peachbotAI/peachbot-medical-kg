from schema.clinical_schema import *
from schema.enums import *
from schema.evidence import Evidence
from schema.validators import validate_knowledge_unit


def test_valid_ku():
    ku = ClinicalKnowledgeUnit(
        inputs=ClinicalInputs(symptoms=["fever", "cough"]),
        context=ClinicalContext(
            severity=Severity.MODERATE,
            duration=Duration.ACUTE,
            system=System.RESPIRATORY
        ),
        signal=ClinicalSignal(
            id="respiratory_infection_pattern",
            priority="moderate"
        ),
        meta=ClinicalMeta(
            weight=3,
            confidence=0.8,
            explanation="Fever with cough suggests respiratory infection"
        ),
        evidence=[
            Evidence(
                source="Harrison’s Principles of Internal Medicine",
                concept="Fever and cough are common in respiratory infections",
                level=EvidenceLevel.TEXTBOOK,
                strength=EvidenceStrength.HIGH
            )
        ]
    )

    assert validate_knowledge_unit(ku)