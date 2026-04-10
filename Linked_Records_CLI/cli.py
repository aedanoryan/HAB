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


def prompt_value(prompt, cast, lower = False):
    raw = input(prompt)
    if lower == True:
        raw.lower()
    try: 
        cast(raw)
        return raw
    except ValueError:
        print("Invalid type")



def prompt_tags():
    tags = []
    while True:
        new = ("Add a new tag; type 'done' when finished").lower()
        if new in tags:
            print("Already in tags")
            continue
        if new == "done":
            break
        tags.append(new)
    return tags

def prompt_metadata():
    
    cb = input("created_by: >").lower()

    notes = input("notes: >").lower()
    meta_d = {"created_by": cb, "notes": notes}
    return meta_d

def main(argv):
    parser = build_parser()
    args = parser.parse_args(argv)
    records = create_records(args.root)

    if args.cmd == "inpsect collection":
        print("These are the current records:")
        for record_name in records.collection:
            print(record_name)



    elif args.cmd == "inspect record":
        print("These are the current records:")
        for record_name in records.collection:
            print(record_name)
        while True:
            insp = input("Select a record to inspect:>").lower()
            if insp not in records.collection:
                print("Please select a record from the list")
                continue
            else:
                break
        inspector = records.collection[insp]
        print(f'Priority: {inspector[""]}')
        print(f'Status: {inspector[""]}')
        print(f'Tags: {inspector[""]}')
        print(f'Metadata: created_by = {inspector["metadata"]["created_by"]}, notes = {inspector["metadata"]["notes"]}')

    elif args.cmd == "add record":
        add_name = prompt_value("Select name for record: >", str, lower=True)
        add_pri = prompt_value("Select priority:>", int)
        add_stat = prompt_value("Select status:>", str, lower=True)
        add_tags = prompt_tags()
        add_meta = prompt_metadata()
        records.add_record(add_name, add_pri, add_stat, add_tags, add_meta)
        save_file(args.root, records)

    elif args.cmd == "remove record":
        print("These are the current records:")
        for record_name in records.collection:
            print(record_name)
        while True:    
            removed = input("Select the record you would like to remove: >").lower()
            if removed not in records.collection:
                print("Please enter a record from the list")
                continue
            records.remove(removed)
            break
        save_file(args.root, records)


    elif args.cmd == "update record":
        print("These are the current records:")
        for record_name in records.collection:
            print(record_name)
        while True:
            up_rec = input("Select a record to update:>").lower()
            if up_rec not in records.collection:
                print("Please select a record from the list")
                continue
            else:
                break
        print("Here are the current values: ")
        inspector = records.collection[up_rec]
        print(f'Priority: {inspector[""]}')
        print(f'Status: {inspector[""]}')
        print(f'Tags: {inspector[""]}')
        print(f'Metadata: created_by = {inspector["metadata"]["created_by"]}, notes = {inspector["metadata"]["notes"]}')
        
        
        
        
          
        
        while True: 
            c_pri = input("Do you want to change Priority ?: Y or N >").upper
            if c_pri == "N":
                up_pri = records.collection[up_rec]["priority"]
                break
            elif c_pri == "Y":
                up_pri = input("Select new  Priority")
                try:
                    int(up_pri)
                    break
                except ValueError:
                    print("Only enter whole numbers")
                continue
            else:
                print("Please enter 'Y' or'N'")
           
        while True:
            
            c_stat = input("Do you want to change Status ?: Y or N >").upper
            if c_stat == "N":
                up_stat = records.collection[up_rec]["status"]
                break
            elif c_stat == "Y":
                up_stat = input("Select Status").lower()
                break
            else:
                print("Please enter 'Y' or'N'")       
        
        
        
        while True:
            c_tag = input("Do you want to change Tags ?: Y or N >").upper()
            if c_tag == "N":
                up_tags = records.collection[up_rec]["tags"]
                break
            elif c_tag == "Y":
                while True:
                    c_add =input("Do you want to add tags? Y or N:>").upper()
                    if c_add == "N":
                        break
                    elif c_add == "Y":
                        while True:
                            up_tags = records.collection[up_rec]["tags"]
                            new_tag = ("Please enter tags; enter 'done' when finished")
                            if new_tag in up_tags:
                                print("Tag already added")
                                continue
                            if new_tag == "done":
                                break
                            up_tags.append[new_tag]
                while True:        
                    c_rem = input("Do you want to remove tags?")
                    if c_rem == "N":
                        break
                    elif c_rem == "Y":
                        print("")

                
                            
            else:
                print("Please enter 'Y' or'N'")  

        while True:
            c_meta = input("Do you want to change Metadata ?: Y or N >").upper
            if c_meta == "N":
                up_meta = records.collection[up_rec]["metadata"]
                break
            elif c_meta == "Y":
                cb = input("Select value for Metadata: created_by:").lower()
                notes = input("Select value for Metadata: notes")
                up_meta = {"created_by": cb, "notes": notes}
                break
            else:
                print("Please enter 'Y' or'N'")  

        current = records.collection[up_rec]
        current.update(up_pri, up_stat, up_tags, up_meta)
        name_change = input("Do you want to change this record's name? Y or N")
        if name_change == "N":
            save_file(args.root, records)
            return
        elif name_change == "Y": 
            new_name = input("Please select new name: ").lower()
            records.rename(up_rec, new_name)
            save_file(args.root, records)
            return
        else:
            print("Please select between 'Y' and 'N'")

       
       
       
