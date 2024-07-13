# Prog for Reading the file, and it's called =(Outo-closability)
try:
    with open("Hyd.data","r") as fp:
        print("-" * 50)
        print("File Name Opens in read mode")
        print("Type of fp=", type(fp))  # <class '_io.TextIOWrapper'>
        print("------------within with open() as_____________")
        print("File Name=", fp.name)
        print("File Mode=", fp.mode)
        print("Is File Readable=", fp.readable())
        print("Is File Writable=", fp.writable())
        print("Is File Closed=", fp.closed)
        print("-" * 50)
    print("------------after / out-of with open() as_____________")
    print("Now Is File Closed=", fp.closed)
    print("-" * 50)
except FileNotFoundError:
    print("File Does not Exist!")






