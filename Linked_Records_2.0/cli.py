import argparse
from create_records import create_records
from class_def import Record, RecordCollection
from load_save import save_file
def build_parser():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest = "cmd")

    p_in_c = sub.add_parser("inspect collection")
    p_in_c.add_argument("root")

    p_in_r = sub.add_parser("inspect record")
    p_in_r.add_argument("root")

    p_add = sub.add_parser("add record")
    p_add.add_argument("root")

    p_rem = sub.add_parser("remove record")
    p_rem.add_argument("root")

    p_up = sub.add_parser("update record")
    p_up.add_argument("root")

    return parser

def value_prompt(prompt:str, cast:str, lower=False):
    raw = input(prompt)
    if lower == True:
        raw.lower()
    try:
        cast(raw)
        return raw
    except ValueError:
        print("Invalid input")

def tag_prompt():
    tags = []
    while True:
        new = input("Enter new tags one at a time; enter 'done' when finished >").lower()
        if new in tags:
            print("Entry already in tags")
            continue
        if new == "done":
            return tags
        if new == "":
            print("tag cannot be empty")
            continue
        tags.append(new)
    

def meta_prompt():
    cb = input("Enter value for metadata - created_by:> ").lower()
    notes = input("Enter value for metadata - notes: >").lower()
    return  {"created_by" : cb, "notes": notes}




def main(argv):
    parser = build_parser()
    args = parser.parse_args(argv)
    records = create_records(args.root)

    if args.cmd == "inspect collection":
        print("Here are the current records:")
        for record_name in records.collection:
            print(record_name)


    elif args.cmd == "inspect record":
        print("Here are the current records:")
        for record_name in records.collection:
            print(record_name)
        while True:
            insp = input("Select record to inspect:> ").lower()
            if insp not in records.collection:
                print("Please enter a record from the list")
                continue
            else:
                break
        record = records.collection[insp]
        

        inspector = record.inspect()

        print(f'The attributes for {insp} are as follows: ')
        print(f'Priority = {inspector["priority"]}')
        print(f'Status = {inspector["status"]}')
        print(f'Tags = {inspector["tags"]}')
        print(f'Metadata - created_by = {inspector["metadata"]["created_by"]}')
        print(f'Metadata - notes = {inspector["metadata"]["notes"]}')






    elif args.cmd == "add record":
        pass
    elif args.cmd == "remove record":
        pass
    elif args.cmd == "update record":
        pass

