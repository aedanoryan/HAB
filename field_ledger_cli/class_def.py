class RecordCollection():
    def __init__(self, collection):
        self.collection = collection


    def add(self, name, priority, status, tags, metadata):
        self.collection[name] = Record(name, priority, status, tags, metadata)

    def remove(self, removed: str):
        del self.collection[removed]

    def name_change(self, current, new_name):
            self.collection[new_name] = self.collection[current]
            del self.collection[current]
            self.collection[new_name].update("name", new_name)



class Record():
    def __init__(self, name, priority: int, status: str, tags: list, metadata: dict):
        self.name = name
        self.priority = priority
        self.status = status
        self.tags = tags
        self.metadata = metadata 


    def inspect(self):
        inspector = {"name": self.name, "priority": self.priority, 
                     "status": self.status, "tags": self.tags, "metadata": self.metadata
                     }
        return inspector
    def to_dict(self):
        entry = {
        "priority": self.priority, 
        "status": self.status, 
        "tags" : self.tags, 
        "metadata": {
        "created_by": self.metadata["created_by"],
        "notes": self.metadata["notes"]}
        }
      
        return entry

    def update(self, att, new_value, remove = False):
        if att == "priority":
            self.priority = new_value
        elif att == "status":
            self.status = new_value
        elif att == "tags":
            if remove:
                self.tags.remove(new_value)
            else:
                self.tags.append(new_value)
        elif att == "metadata":
            key, value = next(iter(new_value.items()))
            self.metadata[key] = value