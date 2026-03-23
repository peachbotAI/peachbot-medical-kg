import yaml


def load_alias_config():
    with open("configs/aliases.yaml", "r") as f:
        return yaml.safe_load(f)


def build_reverse_index(alias_config):
    """
    Convert alias config into lookup dictionary:
    alias → canonical term
    """

    reverse_map = {}

    for category, terms in alias_config.items():
        for canonical, aliases in terms.items():

            # Map canonical to itself
            reverse_map[canonical] = canonical

            for alias in aliases:
                reverse_map[alias] = canonical

    return reverse_map


def normalize_terms(input_terms):
    """
    Normalize input terms into canonical medical terms
    """

    config = load_alias_config()
    reverse_map = build_reverse_index(config)

    normalized = []

    for term in input_terms:
        term_lower = term.lower().strip()

        if term_lower in reverse_map:
            normalized.append(reverse_map[term_lower])
        else:
            normalized.append(term_lower)  # fallback (keep original)

    return list(set(normalized))  # remove duplicates