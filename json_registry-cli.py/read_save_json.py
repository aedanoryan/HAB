import json
from pathlib import Path
from class_def import Record, RecordCollection

def open_file(file_path: Path):
    with open(file_path, "r") as f:
        opened_file = json.load(f)
        return opened_file
    
def save_file(file_path : Path, collection: RecordCollection):
    new_dict = {}
    for key, record in collection.collection.items():
        new_dict[key] = record.to_dict()
    with open(file_path, "w") as f:
        json.dump(new_dict, f, indent=4)
        

