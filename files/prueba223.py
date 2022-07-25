class a:
    def __init__(self):
        self.x=0
    
class b(a):
    def spam(self):
        print("bspam")
        super().spam()
        return 20
        
casa=a()
masa=b()

print(casa.spam())
print(masa.spam())
