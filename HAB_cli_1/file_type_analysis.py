from pathlib import Path
from collections import Counter

def count_extensions(parsed_path: Path):
    folder = Path(parsed_path)

    ext_dict = Counter(
        i.suffix.lower()
        for i in folder.rglob("*")
        if i.is_file()
    )

    return ext_dict