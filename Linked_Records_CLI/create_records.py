from load_save import load_file
from class_def import Record, RecordCollection
from pathlib import Path

def create_records(file_path: Path):
    dict_form = load_file(file_path)
    populating = {}
    for name, value in dict_form.items():
        populating[name] = Record(name,value["priority"], value["status"], value["tags"], value["metadata"], value["links"])
    records = RecordCollection(populating)
    return records

