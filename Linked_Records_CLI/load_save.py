import json
from pathlib import Path
from class_def import RecordCollection, Record
def load_file(file_path: Path):
    with open(file_path, "r") as f:
        dict_form = json.load(f)
        return dict_form
    
def save_file(file_path: Path, collection: RecordCollection):
    save_dict = {}
    for name, value in collection.collection.items():
        save_dict[name] = value.to_dict()
    with open(file_path, "w") as f:
        json.load(save_dict, f, indent = 4)