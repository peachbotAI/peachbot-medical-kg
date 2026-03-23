import yaml


def load_config(path="configs/config.yaml"):
    """
    Load main pipeline configuration
    """
    with open(path, "r") as f:
        return yaml.safe_load(f)


def load_version_config(path="configs/version.yaml"):
    """
    Load versioning configuration
    """
    with open(path, "r") as f:
        return yaml.safe_load(f)