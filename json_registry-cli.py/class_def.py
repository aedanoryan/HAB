
class RecordCollection():
    def __init__(self, collected: dict):
        self.collection = collected
    
    def inspect(self):
        return self.collection
    
    def add(self, name, attack, defense, heal, target, order):

        new = Record(name, attack, defense, heal, target, order)
        self.collection[new.name] = new
    
    def remove(self, choice: str):
        del self.collection[choice]
                    
            


class Record():
    def __init__(self, name: str, attack: int, defense: int, heal: int, target: str, order: int):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.heal = heal
        self.target = target
        self.order = order

    def to_dict(self):
        entry = {
        "attack": self.attack, 
        "defense": self.defense, 
        "heal": self.heal, 
        "target": self.target, 
        "order": self.order
        }
        return entry
   
    def update(self, field: str, new_value: str):
        if field not in ("attack", "defense", "heal", "target", "order"):
            raise ValueError("Invalid selection.")
        
        if field == "target":
            new_value = new_value.lower()
            if new_value not in ("self", "enemy", "ally"):
                raise ValueError("Invalid selection")
            setattr(self, field, new_value)
        else:
            try: 
                setattr(self, field, int(new_value))
            except:
                raise ValueError("Please select a whole number")
       
       
       
       
       
       
       
       
       
       


    def inspect(self):
        record_dict = {
        "attack": self.attack,
        "defense": self.defense,
        "heal": self.heal,
        "target": self.target,
        "order": self.order,}
        return record_dict
    