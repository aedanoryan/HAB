from load_save import open_file
from pathlib import Path
from class_def import Record, RecordCollection

def create_records(file_path: Path):
    record_dict = open_file(file_path)
    records = {}

    for record_name, record_content in record_dict.items():
        records[record_name] = Record(
            record_content["name"],
            record_content["priority"],
            record_content["status"],
            record_content["tags"],
            record_content["metadata"])

    return RecordCollection(records)
