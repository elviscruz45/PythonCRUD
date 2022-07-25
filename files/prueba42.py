def funciondecoradora(funcionparametro):
    def interiror():
        print("vamos a realizar un calculo")
        funcionparametro()
        
        print("Hemos terminado el calculo")
    
    return interiror

@funciondecoradora
def suma():
    print(20)
    
    
suma()
    
