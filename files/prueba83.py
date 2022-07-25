import csv 


HEAD=["ID","NAME","SUBJECT"]
dict={"ID": "104","NAME":"Johnn","SUBJECT":"Manthematics"}
tmp="hola.tmp"

with open(tmp,"a") as f:
    escribir=csv.DictWriter(f,fieldnames=HEAD)
    escribir.writerow(dict)

