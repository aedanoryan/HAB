
class RecordCollection():
    def __init__(self, collected: dict):
        self.collection = collected
    
    def inpsect(self):
        return self.collection
    
    def add(self):
        name = input("Select attribute name: >").lower()
        attack = int(input("Select attribute attack: >"))
        defense = int(input("Select attribute defense: >"))
        heal = int(input("Select attribute heal: >"))
        target = input("Select attribute target: >").lower()
        order = int(input("Select attribute order: >"))
        new = Record(name, attack, defense, heal, target, order)
        self.collection[new.name] = new 
    
    def remove(self):
        while True:    
            while True:
                print("Here are the following records:")
                for record in self.collection:
                    print(record)
                choice = input("select record to remove: >").lower()
                if choice in self.collection:
                    break
                else:
                    print("Choice not in records")
            while True:
                confirm = input(f"Are you sure you want to remove {choice}? Y or N: >").upper()
                if confirm in ("Y", "N"):
                    if confirm == "N":
                        break
                    elif confirm == "Y":
                        del self.collection[choice]
                        return
                else:
                    print("Please select Y or N")
                    
            


class Record():
    def __init__(self, name: str, attack: int, defense: int, heal: int, target: str, order: int):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.heal = heal
        self.target = target
        self.order = order
    def update(self):
        print(f"These are the current attributes for {self.name}:")
        print(f"attack = {self.attack}, defense = {self.defense}, "
            f"heal = {self.heal}, target = {self.target}, order = {self.order}")

        while True:
            choice = input("Select attribute to modify: > ").lower()
            if choice in ("attack", "defense", "heal", "target", "order"):
                break
            else:
                print("Invalid selection.")

        while True:
            current_value = getattr(self, choice)
            print(f"Current attribute value: {current_value}")
            change = input("Select attribute change: > ").lower()

            if choice == "target":
                if change in ("self", "ally", "enemy"):
                    setattr(self, choice, change)
                    break
                else:
                    print("Invalid selection.")
            else:
                try:
                    setattr(self, choice, int(change))
                    break
                except ValueError:
                    print("Please enter a whole number.")

        print("Updated record:")
        print(
            f"attack = {self.attack}, defense = {self.defense}, "
            f"heal = {self.heal}, target = {self.target}, order = {self.order}"
        )
        

    def inpsect(self):
        record_dict = {
        "attack": self.attack,
        "defense": self.defense,
        "heal": self.heal,
        "target": self.target,
        "order": self.order,}
        return record_dict
    