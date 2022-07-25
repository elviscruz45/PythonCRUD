class softwares:
    names = []
    versions = {}
    
    def __init__(self,names):
        if names:
            self.names=names.copy()
            for name in names:
                self.versions[name]=1
        else:
            raise Exception("Plese enter the names")

p = softwares(['S1','S2','S3'])
p1 = softwares([])

print(p)
print(p1)
