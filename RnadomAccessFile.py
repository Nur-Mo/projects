#Prog for Demonstrating Ramdom Access File:
# 2 function available
# Tell() --> Gives Index of File Pointer
# Seek() --> Will re-set the file Pointer to Specified Index

with open("kvr.data","r") as fp:
    print("Initial Pos of fp=",fp.tell()) #This function of tell()
    filedata = fp.read(6)
    print("File Data=",filedata)# PYTHON
    print("Now Pos of words in fp is=",fp.tell()) # 6
    print("-"*50)
    filedata = fp.read(4)
    print("File Data=", filedata) # _IS_
    print("Now Pos of fp=", fp.tell()) # 10
    print("-" * 50)
    filedata = fp.read(3)
    print("File Data=", filedata) # AN
    print("Now Pos of fp=", fp.tell()) # 14
    print("-" * 50)
    print("File Data=", filedata)
    print("Now Pos of fp=", fp.tell())
    print("-" * 50)
    filedata = fp.read()
    print("File Data=", filedata) # LANG AND ALSO FUN LANG
    print("Now Pos of fp=", fp.tell()) # 41
    print("------------------------------------")
    filedata = fp.read()
    print("File Data=", filedata) #NO DATA desply EMPTY DATA (Because it's out of reach data)
    print("Now Pos of fp=", fp.tell()) # 41\
    fp.seek(0) # SEEK will re-set complete data
    filedata = fp.read()
    print("File Data=", filedata)
    print("Now Pos of fp=", fp.tell())
    print("------------------------------------")

    # It's easy to access data from a file long except knowing Indexing but you can use
    # These 2 functions of Tell() and Seek()