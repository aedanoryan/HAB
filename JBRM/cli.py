import argparse

from .file_funcs import inspect_ability, add_ability, update_ability, remove_ability

from .read_save_file import read_file, save_file

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
    abilities = read_file()

    if args.cmd == "inspect":
        # all_abilities = inspect_ability(abilities)
        for key in abilities:
            print(f'{key} has these stats:')
            for stat, value in abilities[key].items():
                print(f' {stat}: {value}') 

    elif args.cmd == "add":
        new_abilities = add_ability(abilities)
        save_file(new_abilities)
        print("ability added")
        
    elif args.cmd == "update":
        updated_abilities = update_ability(abilities)
        save_file(updated_abilities)
        print("ability updated")

    elif args.cmd == "remove":
        updated_abilities = remove_ability(abilities)
        save_file(updated_abilities)
        print("ability removed")

