#Prog for Creating new file (An empty file)
kvr = open("kvr.data","w")
print("File Created newly and opens in write mode")
print("Type of kvr=",type(kvr)) # This's to create file as <class '_io.TextIOWrapper'>
print("-"*50)
try:
    kvr = open("Hyd.data","r")
    print("File Name opened in read mode Successfully..")
except FileNotFoundError:
    print("File doesn't Exist!")