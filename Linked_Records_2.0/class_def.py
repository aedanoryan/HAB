
class RecordCollection():
    def __init__(self, collection):
        self.collection = collection
    
    def add_record(self, name, priority, status, tags, metadata, links):
        self.collection[name] = Record(name, priority, status, tags, metadata, links)

    def remove_record(self, rem):
        del self.collection[rem]





    def rename(self, old_name, new_name):
        self.collection[new_name] = self.collection[old_name]
        del self.collection[old_name]
        self.collection[new_name].update("name", new_name)


class Record:
    def __init__(self, name, priority, status, tags, metadata, links):
        self.name = name
        self.priority = priority
        self.status = status
        self.tags = tags
        self.metadata = metadata
        self.links = links
    
    def to_dict(self):
        entry = {
        "priority": self.priority, 
        "status": self.status, 
        "tags" : self.tags, 
        "metadata": {
        "created_by": self.metadata["created_by"],
        "notes": self.metadata["notes"]},
        "links": self.links 
        }
      
        return entry
    def inspect(self):
        inspector = {
        "priority": self.priority, 
        "status": self.status, 
        "tags" : self.tags, 
        "metadata": self.metadata
        }
        return inspector

    def update(self, att:str, new_value):
        if att == "name":
            self.name = new_value

        elif att == "priority":
            self.priority = new_value

        elif att == "status":
            self.status = new_value

        elif att =="tags":
            self.tags = new_value

        elif att == "metadata":
            if "created_by" in new_value:
                self.metadata["created_by"] = new_value["created_by"]
            if "notes" in new_value:
                self.metadata["notes"] = new_value["notes"]
        
        elif att == "links":
            self.links = new_value