import json
import yaml
from pathlib import Path


def parse_file(filepath):
    path = Path(filepath)
    suffix = path.suffix.lower()

    content = path.read_text()

    if suffix == ".json":
        return json.loads(content)

    if suffix in (".yml", ".yaml"):
        return yaml.safe_load(content)

    raise ValueError(f"Unsupported file format: {suffix}")
