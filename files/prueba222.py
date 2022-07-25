class a:
    def spam(self):
        print("aspam")
        return(10)
    
class b(a):
    def spam(self):
        print("bspam")
        super().spam()
        return 20
        
casa=a()
masa=b()

print(casa.spam())
print(masa.spam())
