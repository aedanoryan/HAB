from class_def import Record, RecordCollection

from read_save_json import open_file


file_path = "C:\Users\aedan\Desktop\Python\HAB\json_registry-cli.py\sample.json"


def create_records():
    record_dict = open_file(file_path)
    record_objects = {}
    for record_name, record_data in record_dict.items():
        record_obj =Record(record_name, record_data["attack"], record_data["defense"], record_data
               ["heal"], record_data["target"], record_data["order"])
        record_objects[record_obj.name] = record_obj

    collected = RecordCollection(record_objects)
    return collected