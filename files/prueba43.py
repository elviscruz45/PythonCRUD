
def decoradora1():
    pass

def decoradora2(funcion):
    def interno2():
        print("inicio de la operacion")
        print(funcion())
        print("fin de la operacion")
    
    return interno2
    
    



@decoradora2
def suma():
    return 10

suma()