from pathlib import Path
import json

def open_file(file_path: Path):
    with open(file_path, "r") as f:
        file_dict = json.load(f)
        return file_dict

def save_file():
    pass