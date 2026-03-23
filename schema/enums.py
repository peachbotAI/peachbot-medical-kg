"""
Clinical Enumerations for PeachBot Medical Knowledge Graph

These enums represent standardized abstractions derived from:

Primary References:
- Harrison’s Principles of Internal Medicine, 21st Edition
- Oxford Handbook of Clinical Medicine
- WHO Clinical Guidelines
- CDC Clinical Frameworks
- NICE Clinical Guidelines

Note:
These are NOT direct copies of any single textbook taxonomy.
They are normalized categories designed for:
- clinical reasoning
- edge-compatible knowledge systems
- deterministic rule-based inference

All usage must remain consistent with evidence-backed medical knowledge.
"""

from enum import Enum


class Severity(str, Enum):
    """
    Clinical severity classification.

    Derived from:
    - General clinical triage frameworks (WHO, CDC)
    - Standard bedside assessment practice

    Interpretation:
    - LOW → mild / non-threatening
    - MODERATE → clinically significant
    - HIGH → potentially severe / urgent
    """
    LOW = "low"
    MODERATE = "moderate"
    HIGH = "high"


class Duration(str, Enum):
    """
    Temporal classification of clinical presentation.

    Derived from:
    - Harrison’s Internal Medicine (acute vs chronic disease patterns)
    - Standard clinical teaching

    Interpretation:
    - ACUTE → sudden onset, short duration
    - SUBACUTE → intermediate progression
    - CHRONIC → long-standing condition
    """
    ACUTE = "acute"
    SUBACUTE = "subacute"
    CHRONIC = "chronic"


"""
System classification aligned with ICD-10 chapters (WHO).

Reference:
- WHO ICD-10 Version 2019
- https://icd.who.int/browse10/2019/en

Note:
This is a simplified mapping for clinical reasoning.
Each system corresponds to one or more ICD-10 chapters.
"""

from enum import Enum


class System(str, Enum):
    """
    ICD-10 aligned system classification.
    """

    INFECTIOUS_DISEASES = "infectious_diseases"         # A00–B99
    NEOPLASMS = "neoplasms"                             # C00–D49
    BLOOD_IMMUNE = "blood_immune"                       # D50–D89
    ENDOCRINE_METABOLIC = "endocrine_metabolic"         # E00–E89
    MENTAL_BEHAVIORAL = "mental_behavioral"             # F01–F99
    NERVOUS_SYSTEM = "nervous_system"                   # G00–G99
    EYE = "eye"                                         # H00–H59
    EAR = "ear"                                         # H60–H95
    CIRCULATORY = "circulatory"                         # I00–I99
    RESPIRATORY = "respiratory"                         # J00–J99
    DIGESTIVE = "digestive"                             # K00–K95
    SKIN = "skin"                                       # L00–L99
    MUSCULOSKELETAL = "musculoskeletal"                 # M00–M99
    GENITOURINARY = "genitourinary"                     # N00–N99
    PREGNANCY = "pregnancy"                             # O00–O99
    PERINATAL = "perinatal"                             # P00–P96
    CONGENITAL = "congenital"                           # Q00–Q99
    SYMPTOMS_SIGNS = "symptoms_signs"                   # R00–R99
    INJURY_POISONING = "injury_poisoning"               # S00–T98
    EXTERNAL_CAUSES = "external_causes"                 # V01–Y98
    HEALTH_STATUS = "health_status"                     # Z00–Z99
    
class EvidenceLevel(str, Enum):
    """
    Source type classification.

    Hierarchy of medical evidence sources:
    - TEXTBOOK → foundational knowledge (e.g., Harrison’s)
    - GUIDELINE → clinical recommendations (WHO, NICE, CDC)
    - JOURNAL → research evidence (NEJM, Lancet, JAMA)
    """
    TEXTBOOK = "textbook"
    GUIDELINE = "guideline"
    JOURNAL = "journal"


class EvidenceStrength(str, Enum):
    """
    Strength of evidence.

    Derived from:
    - Evidence-based medicine frameworks

    Interpretation:
    - LOW → limited or observational support
    - MODERATE → consistent but not definitive
    - HIGH → strong, widely accepted clinical evidence
    """
    LOW = "low"
    MODERATE = "moderate"
    HIGH = "high"