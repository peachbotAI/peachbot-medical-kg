from schema.clinical_schema import (
    ClinicalInputs,
    ClinicalContext,
    ClinicalSignal,
    ClinicalMeta,
    ClinicalKnowledgeUnit,
)
from schema.evidence import Evidence
from rules.clinical_rule import ClinicalRule


def build_rule(
    *,
    symptoms=None,
    signs=None,
    investigations=None,
    severity,
    duration,
    system,
    signal_id,
    priority,
    weight,
    confidence,
    explanation,
    tags=None,
    evidence: list[Evidence],
):
    """
    High-level builder for creating clinical rules.
    """

    inputs = ClinicalInputs(
        symptoms=symptoms or [],
        signs=signs or [],
        investigations=investigations or [],
    )

    context = ClinicalContext(
        severity=severity,
        duration=duration,
        system=system,
    )

    signal = ClinicalSignal(
        id=signal_id,
        priority=priority,
    )

    meta = ClinicalMeta(
        weight=weight,
        confidence=confidence,
        tags=tags or [],
        explanation=explanation,
    )

    ku = ClinicalKnowledgeUnit(
        inputs=inputs,
        context=context,
        signal=signal,
        meta=meta,
        evidence=evidence,
    )

    return ClinicalRule(ku)