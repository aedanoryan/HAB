from pathlib import Path
import json
from class_def import RecordCollection

def open_file(file_path: Path):
    with open(file_path, "r") as f:
        file_dict = json.load(f)
        return file_dict

def save_file(file_path: Path, collection: RecordCollection):
    new_dict = {}

    for key, value in collection.collection.items():
        new_dict[key] = value.to_dict()
    with open(file_path, "w") as f:
        json.dump( new_dict, f,  indent=4)