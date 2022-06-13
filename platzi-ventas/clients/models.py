import uuid

class Client:
    def __init___(self,name,company,email,position,uid=None):
        self.name=name
        self.company=company
        self.email=email
        self.position=position
        self.uid=uid or uuid.uuid4()
        
    def to_dict(self):
        return vars(self)