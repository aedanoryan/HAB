from pathlib import Path

def inspect_file(file_dict : dict ) -> dict: 
    for i in file_dict:
        print(f'Key: {i}')
        