import json
import os
from configs.config_loader import load_version_config


def generate_manifest(output_dir):
    version_cfg = load_version_config()

    manifest = {
        "name": "peachbot-medical-kg",
        "version": version_cfg["version"],
        "files": {
            "knowledge": "medai.json",
            "report": "report.json",
            "metadata": "metadata.json"
        }
    }

    path = os.path.join(output_dir, "manifest.json")

    with open(path, "w") as f:
        json.dump(manifest, f, indent=2)

    print(f"[✓] Manifest generated → {path}")