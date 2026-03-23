from rules.rule_registry import RuleRegistry
from exporters.json_exporter import export_to_json
from exporters.core_mapper import CORE_OUTPUT_PATH

# Import rule sources
from sources.patterns.respiratory_patterns import get_respiratory_rules


def collect_all_rules():
    registry = RuleRegistry()

    # Add rule groups here
    for rule in get_respiratory_rules():
        registry.register(rule)

    return registry


def main():
    registry = collect_all_rules()

    data = registry.to_core_json()

    export_to_json(data, CORE_OUTPUT_PATH)


if __name__ == "__main__":
    main()