import json
from pathlib import Path

import yaml


def parse_file(filepath):
    path = Path(filepath)
    suffix = path.suffix.lower()

    if suffix == ".json":
        content = path.read_text()
        return json.loads(content)

    if suffix in (".yml", ".yaml"):
        content = path.read_text()
        return yaml.safe_load(content)

    raise ValueError(f"Unsupported file format: {suffix}")