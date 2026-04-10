class RecordCollection():
    def __init__(self, collection: dict):
        self.collection = collection
        
    def rename(self, old_name: str, new_name:str):
        self.collection[new_name] = self.collection[old_name] 
        del self.collection[old_name]
        self.collection[new_name].name_change(new_name)

    def remove(self, removed: str):
        del self.collection[removed]

    def add_record(self, name, pri, stat, tags, meta):
        self.collection[name] = Record(name, pri, stat, tags, meta)



class Record():
    def __init__(self, name, priority, status, tags, metadata ,links):
        self.name = name
        self.priority = priority
        self.status = status
        self.tags = tags
        self.metadata = metadata
        self.links = links

    def to_dict(self):
        entry = {"priority": self.priority, "status": self.status, 
                 "tags": self.tags, "metadata": self.metadata, "links": self.links}
        return entry
    
    def name_change(self, new_name):
        self.name = new_name

    def inspect(self, record : str):
        inspector = {
            "priority": self.priority,
            "status": self.status,
            "tags": self.tags,
            "metadata": self.metadata

        }
        return inspector
    
    def update(self, up_pri, up_stat, up_tags, up_meta):
        self.priority = up_pri
        self.status = up_stat
        self.tags = up_tags
        self.metadata = up_meta

