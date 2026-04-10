from load_save import load_file
from class_def import Record, RecordCollection
from pathlib import Path

def create_records(file_path: Path):
    loader = load_file(file_path)
    collection = {}
    for record_name, record in loader.items():
        collection[record_name] = Record(record_name, record["priority"], 
            record["status"], record["tags"], record["metadata"], record["links"])
    records = RecordCollection(collection)
    return records