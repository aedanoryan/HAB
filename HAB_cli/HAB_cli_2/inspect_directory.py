from pathlib import Path
from collections import Counter

def count_file_type(rootpath: Path):
    directory = Path(rootpath)
    
    count = Counter(
        i 
        for i in directory.rglob("*") 
        if i.is_file()
    )
    return count


def show_largest(rootpath: Path):
    pass

def quick_stats(rootpath: Path):
    pass

