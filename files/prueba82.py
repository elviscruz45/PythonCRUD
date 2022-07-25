dict={'ID':5,'NAME':'William','SUBJECT':'Python'}

from csv import DictWriter

headerCSV=["ID","NAME","SUBJECT"]

dict={"ID": "04","NAME":"John","SUBJECT":"Manthematics"}


with open("files1.csv","a",newline="") as f:
    archivo=DictWriter(f,fieldnames=headerCSV)
    archivo.writerow(dict)
    
