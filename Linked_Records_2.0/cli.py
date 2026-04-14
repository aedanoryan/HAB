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
    while True:
        raw = input(prompt)
        if lower == True:
            raw = raw.lower()
        try:
            value =cast(raw)
            return value
        except ValueError:
            print("Invalid input")

def list_prompt(list_name: str):
    list = []
    while True:
        new = input(f"Enter new {list_name} one at a time; enter 'done' when finished >").lower()
        if new in list:
            print(f"Entry already in {list_name}")
            continue
        if new == "done":
            return list
        if new == "":
            print("entry cannot be empty")
            continue
        list.append(new)
    
    

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
            if insp in records.collection:
                record = records.collection[insp]
                break
            print("Please enter a record from the list")
        

        inspector = record.inspect()

        print(f'The attributes for {insp} are as follows: ')
        print(f'Priority = {inspector["priority"]}')
        print(f'Status = {inspector["status"]}')
        print(f'Tags = {inspector["tags"]}')
        print(f'Metadata - created_by = {inspector["metadata"]["created_by"]}')
        print(f'Metadata - notes = {inspector["metadata"]["notes"]}')






    elif args.cmd == "add record":
        name = value_prompt("Please enter name for new record: >", str, lower=True)
        priority = value_prompt("Please enter priority for new record: >", int)
        status = value_prompt("Please enter status for new record: >",str, lower=True)
        tags = list_prompt("tags")
        meta = meta_prompt()
        links = list_prompt("links")

        records.add_record(name, priority, status, tags, meta, links)




    elif args.cmd == "remove record":
        print("Here are the current records:")
        for record_name in records.collection:
            print(record_name)
        while True:
            rem = input("Enter the name of the record you would like to remove:>").lower()
            if rem not in records.collection:
                print("Please enter a valid record")
            else:
                records.remove_record(rem)
                break
        








    elif args.cmd == "update record":
        print("Here are the current records:")
        for record_name in records.collection:
            print(record_name)
        
        done = False
        while done == False:
            while True:
                up_rec = input("Please select a record to update: >").lower()
                if up_rec in records.collection:
                    break
                print("Please select a valid record")
            while True:
                att = input("Select an attribute to update").lower()
                if att in ("name", "priority", "status", "tags", "metadata", "links"):
                    break
                print("Choose between: 'priority', 'status', 'tags', 'metadata', 'links'")
            
            if att == "name": 
                new_name = input("Enter new name for record:>").lower()
                records.rename(up_rec, new_name)
                break
            

            elif att == "priority":
                while True:
                    up_pri =input("Select whole number for priority update: >")
                    try:
                        new_value =int(up_pri)
                        records.collection[up_rec].update(att, new_value)
                        break
                    except ValueError:
                        print("Please enter whole number")

            
            elif att == "status":
                while True:
                    up_stat = input("Select status to update:>").lower()
                    records.collection[up_rec].update(att, up_stat)
                    break
           
           
            elif att == "tags":
                up_tags = records.collection[up_rec].tags

                tags_done = False
                while tags_done == False:
                    print(f"These are the current tags: {up_tags}")
                    
                    while True:
                        check_add = input("Do you want to add tags? Y or N: >").upper()
                        if check_add == "N":
                            break
                        elif check_add == "Y":
                            while True:
                                new_tag = input("Enter new tag")
                                if new_tag in up_tags:
                                    print("Entry already in tags")
                                    continue
                                if new_tag == "":
                                    print("tag cannot be empty")
                                    continue
                                up_tags.append(new_tag)
                                break
                        print("Please enter 'Y' or N'")
                    
                    while True:
                        check_rem = input("Do you want to remove tags? Y or N: >").upper()
                        if check_rem == "N":
                            break
                        elif check_rem == "Y":
                            removed = input("Enter tag to remove:>").lower()
                            while True:
                                if removed not in up_tags:
                                    print("Entry not in tags")
                                    continue
                                else:
                                    up_tags.remove(removed)
                                    break                            
                        print("Please enter 'Y' or N'")
                    
                    
                    while True:    
                        check_done = input("Are you done modifying tags? Y or N").upper()
                        if check_done == "Y":
                            tags_done = True
                            break
                        elif check_done == "N":
                            break
                        print("Please enter 'Y' or 'N'")                        
                records.collection[up_rec].update(att, up_tags)


            elif att == "metadata":
                while True:
                    which = input("Enter '1' to modify created_by; Enter '2' to modify notes: >")
                    if which == "1":
                        cb = input("Enter update for created_by: >").lower()
                        up_meta = {"created_by": cb}
                        records.collection[up_rec].update(att, up_meta)
                        break
                    if which == "2":
                        notes = input("Enter update for notes: >").lower()
                        up_meta = {"notes": notes}
                        records.collection[up_rec].update(att, up_meta)
                        break
                    print("Invalid input, enter '1' or '2' ")

            
            elif att == "links":
                up_links = records.collection[up_rec].links
                links_done = False
                while links_done == False:
                    print(f"These are the current links: {up_links}")
                    
                    while True:
                        check_add = input("Do you want to add link? Y or N: >").upper()
                        if check_add == "N":
                            break
                        elif check_add == "Y":
                            while True:
                                new_link = input("Enter new link")
                                if new_link in up_links:
                                    print("Entry already in links")
                                    continue
                                if new_link == "":
                                    print("link cannot be empty")
                                    continue
                                up_links.append(new_link)
                                break
                        print("Please enter 'Y' or N'")
                    
                    while True:
                        check_rem = input("Do you want to remove links? Y or N: >").upper()
                        if check_rem == "N":
                            break
                        elif check_rem == "Y":
                            removed = input("Enter link to remove:>").lower()
                            while True:
                                if removed not in up_links:
                                    print("Entry not in links")
                                    continue
                                else:
                                    up_links.remove(removed)
                                    break                            
                        print("Please enter 'Y' or N'")
                    while True:    
                        check_done = input("Are you done modifying links? Y or N").upper()
                        if check_done == "Y":
                            links_done = True
                            break
                        elif check_done == "N":
                            break
                        print("Please enter 'Y' or 'N'")                        
                records.collection[up_rec].update(att, up_links)



            while True:
                cont = input("Make another update? Y or N: >").upper()
                if cont == "N":
                    done = True
                    break
                elif cont == "Y":
                    break
                print("Please enter 'Y' or 'N'")
            
    save_file(args.root, records)