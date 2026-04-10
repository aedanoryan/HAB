
class RecordCollection():
    def __init__(self, collection):
        self.collection = collection
    
    def add_record(self):
        pass

    def remove_record(self):
        pass
    def rename(self):
        pass


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
        "notes": self.metadata["notes"]}
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




     

    def update():
        pass