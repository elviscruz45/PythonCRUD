class Coche():
    def __init__(self):
        self.__largoChasis=250
        self.__anchoChasis=120
        self.ruedas=7
        self.__enmarcha=False

    def arrancar(self,arrancamos):
        self.__enmarcha=arrancamos
        if(self.__enmarcha):
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"
        
    def casaca(self):
        return self.ruedas

    def estado(self):
        print("el coche tiene",self.ruedas,"ruedas Un ancho de",self.__anchoChasis,"Y un largo de",self.__largoChasis)
        

micoche=Coche()
micoche.ruedas=1011
print(micoche.ruedas)
print(micoche.estado())
print(micoche.casaca())
