import argparse
from pathlib import Path
from .inspect_directory import count_file_type, show_largest, quick_stats

def build_parser():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers( dest = "cmd")

    p_type = sub.add_parser("type_count")
    p_type.add_argument("root")

    p_large = sub.add_parser("largest")
    p_large.add_argument("root")

    p_quick = sub.add_parser("stats")
    p_quick.add_argument("root")

    return parser


def main(argv):
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.cmd == "type_count":
        type_counter = count_file_type(args.root)
        for i in type_counter:
            print(f"There are {type_counter[i]} files with the extension {i}")
    
    elif args.cmd == "largest":
        largest_count = show_largest(args.root)
        for f in largest_count:
            print(f'{f.name} is {f.stat().st_size} bytes large' )
    elif args.cmd == "stats":
        stats = quick_stats(args.root)
        print(f" Total Files : {stats["total_files"]}; Total Size : {stats["total_size"]} bytes ; Total Directories : {stats["total_directories"]}")