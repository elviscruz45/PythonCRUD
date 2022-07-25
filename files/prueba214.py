class point:
    x = None
    y = None
    
    def __init__(self, x , y):
        self.x = x
        self.y = y
    
    def __str__(self):
        s = f'({self.x},{self.y})'
        return s
    def __add__(self,p2):
        x = self.x + p2.x
        y = self.y + p2.y
        return point(x,y)
        
    def __iadd__(self,p2):
        self.x += p2.x
        self.y += p2.y
        return self
    
    def __call__(self):
        print(f"Called Point {self.x},{self.y}")


p1 = point(5,4)
p2 = point(2,3)




p1()
print(p1)
p1.__call__()