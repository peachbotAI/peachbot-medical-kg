from builders.rule_builder import build_rule
from schema.enums import Severity, Duration, System, EvidenceLevel, EvidenceStrength
from schema.evidence import Evidence


def get_respiratory_rules():

    rules = []

    # 🔹 Rule 1: Basic respiratory infection pattern
    rules.append(
        build_rule(
            symptoms=["fever", "cough"],
            severity=Severity.MODERATE,
            duration=Duration.ACUTE,
            system=System.RESPIRATORY,
            signal_id="respiratory_infection_pattern",
            priority="moderate",
            weight=3,
            confidence=0.8,
            explanation="Fever with cough suggests respiratory infection pattern",
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
    )

    # 🔹 Rule 2: Severe respiratory involvement
    rules.append(
        build_rule(
            symptoms=["fever", "cough", "shortness_of_breath"],
            signs=["tachypnea"],
            severity=Severity.HIGH,
            duration=Duration.ACUTE,
            system=System.RESPIRATORY,
            signal_id="lower_respiratory_involvement",
            priority="high",
            weight=5,
            confidence=0.9,
            explanation="Combination suggests lower airway involvement and possible severity",
            tags=["critical_pattern"],
            evidence=[
                Evidence(
                    source="Harrison’s Principles of Internal Medicine",
                    concept="Dyspnea with fever suggests lower respiratory pathology",
                    level=EvidenceLevel.TEXTBOOK,
                    strength=EvidenceStrength.HIGH,
                )
            ],
        )
    )

    return rules