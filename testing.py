
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
my_path = Path(r"C:\Users\aedan\Desktop\Maxone backup")
ext_dict =count_extensions(my_path)
for i in ext_dict:
        print(f"There are {ext_dict[i]} files with the extension {i}")