from pathlib import Path
from collections import Counter

def count_file_type(rootpath: Path):
    directory = Path(rootpath)
    
    count = Counter(
        i.suffix.lower()
        for i in directory.rglob("*") 
        if i.is_file()
    )
    return count


def show_largest(rootpath: Path):
    directory = Path(rootpath)
    files = [p for p in directory.rglob("*") if p.is_file()]

    largest_list = sorted(

        files,
        key = lambda p:p.stat().st_size,
        reverse=True

    )[:5]
    
    return largest_list



def quick_stats(rootpath: Path):
    root = Path(rootpath)
    stats = {"total_files": 0, "total_size": 0, "total_directories": 0}
    for i in root.rglob("*"):
        if i.is_file():
            stats["total_files"] += 1
            stats["total_size"] += i.stat().st_size
        elif i.is_dir():
            stats["total_directories"] += 1
    return stats