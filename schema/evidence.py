from dataclasses import dataclass
from schema.enums import EvidenceLevel, EvidenceStrength


@dataclass
class Evidence:
    source: str              # e.g., Harrison’s Principles of Internal Medicine
    concept: str             # What idea supports this rule
    level: EvidenceLevel     # textbook / guideline / journal
    strength: EvidenceStrength  # low / moderate / high

    reference: str = ""      # optional: DOI / chapter / URL