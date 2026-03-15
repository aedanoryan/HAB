import argparse

from .file_funcs import inspect_ability, add_ability, update_ability, remove_ability

def build_parser():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd")

    sub.add_parser("inspect")
   
    sub.add_parser("add")
   
    sub.add_parser("update")
   
    sub.add_parser("remove")
    
    return parser 

def main(argv):
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.cmd == "inspect":
        all_abilities = inspect_ability()
        for key in all_abilities:
            print(f'{key} has these stats:')
            for stat, value in all_abilities[key].items():
                print(f'     {stat}: {value}') 
    elif args.cmd == "add":
        pass
    elif args.cmd == "update":
        pass
    elif args.cmd == "remove":
        pass

