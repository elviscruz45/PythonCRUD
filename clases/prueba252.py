
import enum
from tkinter.font import names


def prime_numbers(n):
    listas=[True for i in range(n)]
    primos=[]
    
    a=2
    while a<=n:        
        for i in range(a,n,a):
            if i ==a:
                continue
            else:                    
                listas[(i)]=False
        a+=1
 
            
    
    for x,y in enumerate(listas):
        if y==True:
            primos.append(x)

    return primos
    
    
print(prime_numbers(100))
