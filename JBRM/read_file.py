import json

from pathlib import Path


def read_file():
    path = Path(__file__).parent / "abil.json"
    with open(path, "r") as f:
        abil_dict = json.load(f)
    return abil_dict