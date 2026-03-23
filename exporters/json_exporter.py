import json
import os


def export_to_json(data: list, output_path: str):
    """
    Export rules to JSON file.
    """

    # Ensure directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print(f"[✓] Exported {len(data)} rules → {output_path}")