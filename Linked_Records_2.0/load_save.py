from pathlib import Path
from class_def import RecordCollection
import json

def load_file(file_path):
    with open(file_path, "r") as f:
        load_dict = json.load(f)
        return load_dict
    
def save_file(file_path: Path, records: RecordCollection):
    final = {}
    for record_name, record in records.collection.items():
        final[record_name] = record.to_dict()
    with open(file_path, "w") as f:
        json.dump(final, f, indent=4)