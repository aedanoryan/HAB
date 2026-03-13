import argparse
from pathlib import Path

def build_parser():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers( dest = "cmd")

    p_a = sub.add_parser("task1")
    p_a.add_argument("arg1")

    p_b = sub.add_parser("task2")
    p_b.add_argument("")
def main(argv):
    parser = build_parser
    args = parser.parse_args(argv)
