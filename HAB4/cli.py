import argparse


def build_parser():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest= "cmd")

    p_inspect = sub.add_parser("inspect")
    p_inspect.add_argument("root")

    p_add = sub.add_parser("add")
    p_add.add_argument("root")
    
    p_update = sub.add_parser("update")
    p_update.add_argument("root")
    
    p_remove = sub.add_parser("remove")
    p_remove.add_argument("root")
    

    p_query = sub.add_parser("query")
    p_query.add_argument("root")

    p_summary = sub.add_parser("summary")
    p_summary.add_argument("root")


    return parser

def main(argv):
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.cmd == "inspect":
        pass

    elif args.cmd == "add":
        pass

    elif args.cmd == "update":
        pass

    elif args.cmd == "remove":
        pass

    elif args.cmd == "query":
        pass

    elif args.cmd == "summary":
        pass

    
