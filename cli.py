from pathlib import Path

import argparse

from .file_type_analysis import count_extensions


def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    return parser


def main(argv):
    parser = build_parser()
    parsed = parser.parse_args(argv)
    parsed_path = Path(parsed.path)
    extensions =count_extensions(parsed_path)
    for i in extensions:
        print(f"There are {extensions[i]} files with the extension {i}")