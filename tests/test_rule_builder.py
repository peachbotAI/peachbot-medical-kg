from builders.rule_builder import build_rule
from schema.enums import Severity, Duration, System, EvidenceLevel, EvidenceStrength
from schema.evidence import Evidence


def test_rule_builder():

    rule = build_rule(
        symptoms=["fever", "cough"],
        severity=Severity.MODERATE,
        duration=Duration.ACUTE,
        system=System.RESPIRATORY,
        signal_id="respiratory_infection_pattern",
        priority="moderate",
        weight=3,
        confidence=0.8,
        explanation="Fever with cough suggests respiratory infection",
        tags=["infection_risk"],
        evidence=[
            Evidence(
                source="Harrison’s Principles of Internal Medicine",
                concept="Fever and cough are common in respiratory infections",
                level=EvidenceLevel.TEXTBOOK,
                strength=EvidenceStrength.HIGH,
            )
        ],
    )

    data = rule.to_core_format()

    assert data["conditions"]["symptoms"] == ["fever", "cough"]
    assert data["signal"]["id"] == "respiratory_infection_pattern"