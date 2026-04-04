import argparse

from create_records import create_records, save_records

from class_def import RecordCollection, Record

from read_save_json import save_file

def build_parser():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest = "cmd")

    p_inspect_c = sub.add_parser("inspect_collection")
    p_inspect_c.add_argument("root")

    p_inspect_r = sub.add_parser("inspect_record")
    p_inspect_r.add_argument("root")

    p_add = sub.add_parser("add_record")
    p_add.add_argument("root")

    p_rem = sub.add_parser("remove_record")
    p_rem.add_argument("root")

    p_up = sub.add_parser("update_record")
    p_up.add_argument("root")

    return parser

def prompt_value(prompt: str, cast=str, lower=False):
    raw = input(prompt)

    if lower:
        raw = raw.lower()
    
    if raw == "cancel":
        return None
    
    try:
        return cast(raw)
    except ValueError:
        print("Please enter a valid value")
        return "retry"







def main(argv):
    parser = build_parser()
    args = parser.parse_args(argv)
    collection = create_records(args.root)
    print("At any point, type 'cancel' to exit program")
    

    if args.cmd == "inspect_collection":
        print("These are the following records:")
        for key in collection.collection:
            print(key)


    elif args.cmd == "inspect_record":
        while True:
            choice = input("select record to inspect: >").lower()
            if choice == "cancel":
                return
            elif choice in collection.collection:
                record = collection.collection[choice]
                inspector = record.inspect()
                for key, value in inspector.items():
                    print(f"{key}: {value}")
                break
            else:
                print("record does not exist")

    elif args.cmd == "add_record":
        while True:
            name = prompt_value("Select attribute name: >", str, lower=True)
            if name is None:
                return
            if name == "retry":
                continue
            break

        while True:
            attack = prompt_value("Select attribute attack: >", int)
            if attack is None:
                return
            if attack == "retry":
                continue
            break
        while True:
            defense = prompt_value("Select attribute defense >", int)
            if defense is None:
                return
            if defense == "retry":
                continue
            break

        while True:
            heal = prompt_value("Select attribute heal: >", int)
            if heal is None:
                return
            if heal == "retry":
                continue
            break
        while True:
            target = prompt_value("Select attribute target: >", str, lower=True)
            if target is None:
                return
            if target == "retry":
                continue
            if target not in ("self", "enemy", "ally"):
                print("Please choose between 'self' 'enemy', or 'ally'")
                continue
            break

        while True:
            order = prompt_value("Select attribute order: >", int)
            if order is None:
                return
            if order == "retry":
                continue
            break
        collection.add(name, attack, defense, heal, target, order,)
        
        save_file(args.root, collection)




    elif args.cmd == "remove_record":
        done = False
        while not done:    
            
            while True:
                print("Here are the following records:")
                for record in collection.collection:
                    print(record)
                choice = input("select record to remove: >").lower()
                if choice == "cancel":
                    return
                if choice in collection.collection:
                    break
                print("Choice not in records")
            
            while True:
                confirm = input(f"Are you sure you want to remove {choice}? Y or N: >").upper()
                if confirm == "CANCEL":
                    return
                if confirm == "Y":
                    collection.remove(choice)
                    done = True
                    break
                if confirm == "N":
                    break
                print("Please select Y or N")
            save_file(args.root, collection)


    elif args.cmd == "update_record":
        while True:
            print("Here are the current records")
            for key in collection.collection:
                print(record)
            record_name = input("Select record to update: >").lower()
            if record_name == "cancel":
                return
            if record_name in collection.collection:
                break
            print("choice not in records")
 
        record = collection.collection[record_name]

        print(f"These are the current attributes for {record.name}:")
        print(
        f"attack = {record.attack}, defense = {record.defense}, "
        f"heal = {record.heal}, target = {record.target}, order = {record.order}")

        while True:
            field = input(" Select attribute to update: >").lower()
            if field == "cancel":
                return
            if field in ("attack", "defense", "heal", "target", "order"):
                break
            print("please select from attack, defense, heal, target, order")
        
        while True:
            current_record = getattr(record, field)
            print(f"current attribute value: {current_record}")
            new_value = input("Select new value: >")
            if new_value == "cancel":
                return
            try:
                record.update(field, new_value)
                break
            except ValueError as e:
                print(e)
        
        print("Updated record:")
        print(
        f"attack = {record.attack}, defense = {record.defense}, "
        f"heal = {record.heal}, target = {record.target}, order = {record.order}")
        save_file(args.root, collection)



















