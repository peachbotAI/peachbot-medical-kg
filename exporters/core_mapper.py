from configs.config_loader import load_config, load_version_config
import os


def get_output_path():
    config = load_config()
    version_cfg = load_version_config()

    version = version_cfg["version"]
    base_dir = config["output"]["base_dir"]
    file_name = config["output"]["file_name"]

    path = os.path.join(base_dir, version, file_name)
    os.makedirs(os.path.dirname(path), exist_ok=True)

    return path