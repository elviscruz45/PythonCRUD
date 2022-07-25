class DogClass:
    def __init__(self,name,color):
        self.name = name
        self.color = color
    
    def bark(self):
        if self.color == "black":
            return True
        else:
            return False
dc = DogClass('rudra','white')
print(dc.__dict__)
# Output: {'name': 'rudra', 'color': 'white'}

DogClass.__dict__

