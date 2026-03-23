import json
from configs.config_loader import load_version_config
import os


def generate_metadata(output_dir, rule_count):
    version_cfg = load_version_config()

    metadata = {
        "version": version_cfg["version"],
        "domain": version_cfg["metadata"]["domain"],
        "author": version_cfg["metadata"]["author"],
        "total_rules": rule_count,
        "compatibility": version_cfg["compatibility"],
        "description": version_cfg["release"]["description"]
    }

    path = os.path.join(output_dir, "metadata.json")

    with open(path, "w") as f:
        json.dump(metadata, f, indent=2)

    print(f"[✓] Metadata generated → {path}")