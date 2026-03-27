import json
from pathlib import Path

def open_file(file_path: Path):
    with open(file_path, "r") as f:
        opened_file = json.load(f)
        return opened_file
    
def save_file(file_path : Path, new_dict: dict):
    with open(file_path, "r") as f:
        revised_file = json.dump(new_dict, f, indent=4)
        return revised_file
