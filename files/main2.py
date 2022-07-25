import csv
import os
import sys

ALMACEN=".clients2.csv"
SCHEMA=["Nombre","Empresa","Correo","Posicion"]
clients=[]


def iniciar_almacen():
    with open(ALMACEN,mode="r") as f:
        reader=csv.DictReader(f,fieldnames=SCHEMA)
        for row in reader:
            clients.append(row)
            
def almacenar():
    tmp="{}.tmp".format(ALMACEN)
    with open(tmp,mode="w") as f:        
        writer=csv.DictWriter(f,fieldnames=SCHEMA)
        writer.writerows(clients)
        os.remove(ALMACEN)
        os.rename(tmp,ALMACEN)
        
        
def recopilar_datos():
    usuarios={
        "Nombre":introducir_datos("name"),
        "Empresa":introducir_datos("empresa"),
        "Correo": introducir_datos("correo"),
        "Posicion": introducir_datos("posicion"),
    }
    return usuarios

def create(valor_creado):
    global clients
    clients.append(valor_creado)
    
    
def Lista():
    global clients
    print("\nId|Nombre       |Empresa           |Correo                           |Posicion          |")
    print("*"*90)
    for u, i in enumerate(clients):
        print(u,"|",i["Nombre"]," "*(10-len(i["Nombre"])),"|",i["Empresa"]," "*(15-len(i["Empresa"])),"|",i["Correo"]," "*(30-len(i["Correo"])),"|",i["Posicion"]," "*(15-len(i["Posicion"])),"|") 


def Update(id_cambio,valor_creado):
    global clients
    
    clients[id]=valor_creado


def Delete(id_cambio,valor_creado):
    global clients
    del clients[id]
    
    
def Search(nombre):
    a=0
    global clients
    for i in clients:
        if i["Nombre"] == nombre:
            print("Si se encuentra en la lista")          
        else:
            a+=1
            
    if a==len(clients):
        print("No se ha encontrado en toda la lista")
        a=0
            


def introducir_datos(dato):    
    datos=""
    while datos=="":
        datos=input(f"cual es tu {dato}?")
    return datos

def inicializacion():
    print("[C]reate client")
    print("[L]ist client")
    print("[U]pdate client")
    print("[D]elete client")
    print("[S]earch client")

if __name__=="__main__":
    
    iniciar_almacen()
    
    print("WELCOME TO PLATZI VENTAS")
    print("*"*50)
    inicializacion()
    inicio=(input("What would you like to do today?")).upper()
    
    if inicio=="C":
        valor_creado=recopilar_datos()
        create(valor_creado)
        
    if inicio=="L":
        Lista()

    if inicio=="U":
        id_cambio= int(input("que item quieres cambiar?"))
        valor_creado=recopilar_datos()
        Update(id_cambio,valor_creado)

    if inicio=="D":
        id_cambio= int(input("que item quieres eliminar?"))
        Delete(id_cambio,valor_creado)
        
    if inicio=="S":
        nombre= (input("que nombre quieres buscar?"))
        Search(nombre)
        
    almacenar()

