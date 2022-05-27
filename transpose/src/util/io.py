import json

from typing import Any

def read_json_value_at_path(path: str, name: str) -> Any:
    with open(path, 'r') as f:
        config = json.load(f)
        return config[name]


def write_json_value_at_path(path: str, name: str, value: Any):
    with open(path, 'r') as f:
        config = json.load(f)
        config[name] = value
    with open(path, 'w') as f:
        json.dump(config, f, indent=4)
