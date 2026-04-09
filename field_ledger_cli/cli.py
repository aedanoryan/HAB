import argparse

from class_def import Record, RecordCollection

from create_records import create_records

from load_save import save_file

def build_parser():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest = "cmd")

    p_insp_coll = sub.add_parser("inspect_collection")
    p_insp_coll.add_argument("root")

    p_insp_rec = sub.add_parser("inspect_record")
    p_insp_rec.add_argument("root")

    p_add = sub.add_parser("add")
    p_add.add_argument("root")

    p_rem = sub.add_parser("remove")
    p_rem.add_argument("root")

    p_up = sub.add_parser("update")
    p_up.add_argument("root")

    return parser

def prompt_value(prompt, cast:str, lower=False):
    raw = input(prompt)

    if lower:
        raw = raw.lower()
    if raw == "cancel":
        return None
    try:
        return cast(raw)
    except ValueError:
        print("Please select valid value")
        return "retry"
    
def prompt_tags():
    tags = []

    print("Enter tags one at a time. Type 'done' when finished")
    while True:
        raw = input("Enter tag: > ").lower()
        if raw == "cancel":
            return None
        if raw =="done":
            return tags
        if raw == "":
            print("tags cannot be empty")
            continue
        if raw in tags:
            print("Tag already exists")
            continue
        tags.append(raw)

def prompt_metadata():
    print("Enter metadata values")

    created_by = input("created_by: >").lower()
    if created_by == "cancel":
        return None
    
    notes = input("notes: >").lower()
    if notes == "cancel":
        return None
    
    return {"created_by": created_by, "notes": notes}

def main(argv):
    parser = build_parser()
    args = parser.parse_args(argv)
    collection = create_records(args.root)
    print("Enter 'cancel' at any point to exit program")

    if args.cmd == "inspect_collection":
        print("Here are the current records:")
        for key in collection.collection:
            print(key)


    if args.cmd == "inspect_record":
        while True:
            record = input("Select record to inspect: >").lower()
            if record == "cancel":
                return
            if record in collection.collection:
                choice = collection.collection[record]
                break
            print("Please select a valid record")
        
        inspector = choice.inspect()
       
        print(f'The attributes for {record} are as follows: ')
        print(f'Priority = {inspector["priority"]}')
        print(f'Status = {inspector["status"]}')
        print(f'Tags = {inspector["tags"]}')
        print(f'Metadata - created_by = {inspector["metadata"]["created_by"]}')
        print(f'Metadata - notes = {inspector["metadata"]["notes"]}')

    if args.cmd == "add":

        while True:
            name = prompt_value("Select value for name", str, lower = True)
            if name is None:
                return
            if name == "retry":
                continue
            break
        while True:
            priority =  prompt_value("Select value for priority", int)
            if priority is None:
                return
            if priority == "retry":
                continue
            break            
    

        while True:
            status=  prompt_value("Select value for status ", str, lower = True)
            if status is None:
                return
            if status == "retry":
                continue
            break
        

        tags =  prompt_tags()
        if tags == None:
            return
        
        metadata = prompt_metadata()
        if metadata == None:
            return
            
        collection.add(name, priority, status, tags, metadata)
        
        save_file(args.root, collection)
        print(f"The record {name} has been added")


    if args.cmd == "remove":
        print("Here are the following records")
        for name in collection.collection:
            print(name)
        removed = input("Select a record to remove: >").lower()
        if removed == "cancel":
            return
        if removed not in collection.collection:
            print("Please select valid record")
        confirm = input(f"Are you sure you want to remove{removed}").upper()
        if confirm == "CANCEL":
            return
        if confirm == "N":
            return
        if confirm == "Y":
            collection.remove(removed)
        save_file(args.root, collection)
        print(f"{removed} successfully removed")
        

    if args.cmd == "update":
        print("Here are the following records")
        for name in collection.collection:
            print(name)
        while True:
            current = input("Select a record to update: >").lower()
            if current == "cancel":
                return
            if current in collection.collection:
                up_rec = collection.collection[current]
                break    
            print("Please select valid record")
        
        while True:    
            att = input("Select attribute to modify (name, priority, status, tags, metadata): >").lower()
            if att == "cancel":
                return 
            if att not in ("name","priority", "status", "tags", "metadata"):
                print("select valid attribute")
            if att == "name":
                new_name = input("Select new name for record: >").lower()
                if new_name == "cancel":
                    return                 
                collection.name_change(current, new_name)
                break
            elif att == "priority":
                new_prior = input("Select priority change: >")
                if new_prior == "cancel":
                    return                 
                up_rec.update(att, (int(new_prior)), remove = False)
                break
            elif att == "status":
                new_status = input("Select status change").lower()
                if new_status == "cancel":
                    return
                up_rec.update(att, str(new_status), remove = False)
                break
            elif att == "tags":
                done = False
                while done == False:
                    print(f"Here are the current tags for {current}:")
                    print(up_rec.tags)
                    while True:
                        r = input("Do you want to remove any tags? Y or N: >").upper()
                        if r == "CANCEL":
                            return
                        if r == "N":
                            break
                        if r == "Y":
                            while True:    
                                axed = input("Selected a tag to remove: >").lower()
                                if axed == "cancel":
                                    return
                                if axed in up_rec.tags:
                                    up_rec.update(att, axed, remove = True)
                                    break
                                else:
                                    print("Please select a valid tag")
                
                        print("Please enter 'Y' or 'N'")
                
                    while True:
                        a = input("Do you want to add any tags? Y or N: >").upper()
                        if a == "CANCEL":
                            return                        
                        if a == "N":
                            break
                        if a == "Y":
                            while True:
                                added = input("What new tag would you like to enter?: >").lower()
                                if added == "cancel":
                                    return
                                up_rec.update(att, added, remove = False)
                                break
                        print("Please enter 'Y' or ''N")
                    while True:
                        finish = input("Finish updating tags? Y or N: >").upper()
                        if finish == "CANCEL":
                            return                        
                        if finish == "N":
                           break
                        if finish == "Y":
                            done = True
                            break
                        if finish not in ("N", "Y"):
                            print("Please enter 'Y' or 'N'")
                break

            elif att == "metadata":
                while True:
                    which = input("Do you want to modify 'created_by' or 'notes'? >").lower()
                    if which == "created_by":
                        new_value = input("Select a new value for 'created_by': >").lower()
                        new_pair = {which: new_value}
                        up_rec.update(att, new_pair, remove = False)
                        break
                    elif which == "notes":
                        if which == "notes":
                            new_value = input("Select a new value for 'notes': >").lower()
                            new_pair = {which: new_value}
                            up_rec.update(att, new_pair, remove = False)
                            break
                    elif which == "cancel":
                        return
                    else:
                        print("Please select between 'created_by' and 'notes'")

            else:
                print("Please select a valid attribute")

        save_file(args.root, collection)
                    

            
            
        