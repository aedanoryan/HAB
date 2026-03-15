from read_file import read_file


def inspect_ability():
    abilities = read_file()
    return abilities



def add_ability():
    abilities = read_file()
   
    name = input("Select name: ").lower()
    attack = int(input("Select attack: "))
    defense = int(input("Select defense: "))
    heal = int(input("Select heal: "))
    target = input("Select target (enemy/ally): ").lower()
    order = int(input("Select order: "))

    abilities[name] = {
    "attack": attack,
    "defense": defense,
    "heal": heal,
    "target": target,
    "order": order   }  

    return abilities



def update_ability():
    abilities = read_file()
    update = ""
    while True:
        choice =input(f' Choose an ability to update: {", ".join(abilities)}  >').lower()
        if choice in abilities:
            update = choice 
            break
        else:
            print("Invalid selection")

    print(f"These are the current stats for {update}")

    for key , value in abilities[update].items():
        print(f"{key}: {value}")
    while True:
        choice = input()
        if choice in 

        else:
            print("Invalid selection")

def remove_ability():
    abilities = read_file()

update_ability()