from rules.rule_registry import RuleRegistry
from exporters.json_exporter import export_to_json
from exporters.core_mapper import get_output_path
from exporters.report_generator import generate_report
from configs.config_loader import load_config
import os

# sources
from sources.patterns.respiratory_patterns import get_respiratory_rules


def collect_all_rules():
    registry = RuleRegistry()

    for rule in get_respiratory_rules():
        registry.register(rule)

    return registry


def main():
    config = load_config()

    registry = collect_all_rules()
    rules = registry.get_all()

    output_path = get_output_path()

    # Export JSON
    data = registry.to_core_json()
    export_to_json(data, output_path)

    # Generate validation report
    if config["validation"]["generate_report"]:
        output_dir = os.path.dirname(output_path)
        generate_report(rules, output_dir)


if __name__ == "__main__":
    main()