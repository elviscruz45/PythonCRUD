
class Date:
    def __init__(self, a):
                self.a = a

    def __format__(self,vaca):
        vaca="paca"
        casa = "mama"
        hola=vaca+casa
        return hola

d = Date(145)

print(format(d))
