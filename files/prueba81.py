from csv import writer

lista=["03","Smith","Science"]

with open("files1.csv","a",newline="") as f:
    write=writer(f)
    write.writerow(lista)
    