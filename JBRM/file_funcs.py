


def inspect_ability(abilities: dict):
    return abilities



def add_ability(abilities: dict):
    
   
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





def update_ability(abilities: dict):
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

        choice = input("Select attribute to update: >")
        if choice in abilities[update]:
            while True: 
                change = input("Selection attribute change: >").lower()
                while True:
                    if change == "target":
                        if change in ("enemy", "ally"):
                            abilities[update][choice] = change
                            return abilities
                        else:
                            print("Invalid selection") 
                    
                    else:
                        try: 
                            abilities[update][choice] = int(change)
                            return abilities
                        except ValueError:
                            print("Invalid selecton")

        else:
            print("Invalid selection")





def remove_ability(abilities: dict):
    while True:
        print("Select an ability from the following to remove:")
        for key in abilities:
            print(key)
        choice = input(">").lower()
        if choice in abilities:
           while True:
                confirm =input(f"Are you sure you want to remove {choice}? Y or N :").upper()
                if confirm == "Y":
                    del abilities[choice]
                    return abilities
                if confirm not in ("Y", "N"):
                    print("Invalid selection")
                elif confirm == "N":
                    break
                else:
                    print("Invalid selection")
            
        else:
            print("Invalid seleciton")
    


