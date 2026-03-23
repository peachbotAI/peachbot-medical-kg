import rules
import os
from rules.rule_registry import RuleRegistry
from exporters.json_exporter import export_to_json
from exporters.core_mapper import get_output_path
from exporters.report_generator import generate_report
from configs.config_loader import load_config
from exporters.metadata_generator import generate_metadata
from exporters.manifest_generator import generate_manifest


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

    # Define output_dir EARLY
    output_dir = os.path.dirname(output_path)

    # Export JSON (core knowledge)
    data = registry.to_core_json()
    export_to_json(data, output_path)

    # Metadata generation
    generate_metadata(output_dir, len(rules))

    # Manifest generation (NEW)
    generate_manifest(output_dir)

    # Validation report
    if config["validation"]["generate_report"]:
        generate_report(rules, output_dir)


if __name__ == "__main__":
    main()