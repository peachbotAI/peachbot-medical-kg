from dataclasses import dataclass, field
from typing import List

from schema.enums import Severity, Duration, System
from schema.evidence import Evidence


@dataclass
class ClinicalInputs:
    symptoms: List[str] = field(default_factory=list)
    signs: List[str] = field(default_factory=list)
    investigations: List[str] = field(default_factory=list)


@dataclass
class ClinicalContext:
    severity: Severity
    duration: Duration
    system: System


@dataclass
class ClinicalSignal:
    id: str                  # e.g., "lower_respiratory_involvement"
    priority: str            # low / moderate / high
    type: str = "clinical_pattern"


@dataclass
class ClinicalMeta:
    weight: int
    confidence: float        # 0.0 – 1.0
    tags: List[str] = field(default_factory=list)
    explanation: str = ""


@dataclass
class ClinicalKnowledgeUnit:
    inputs: ClinicalInputs
    context: ClinicalContext
    signal: ClinicalSignal
    meta: ClinicalMeta
    evidence: List[Evidence]