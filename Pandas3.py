# Prog for reading the Data from CSV file with normal file library
#Non-CSV
try:
  with open("noor.csv","r") as fp:
      csvdata = fp.read()
      print(csvdata)
except FileNotFoundError:
    print("File Doesn't exist")
    print("---------------------------")

# Reading the data using as List type
import csv
try:
    with open("kvr.data","r") as fp:
        csv = csv.reader(fp)
        for record in csv:
            for val in record:
                print("\t{}".format(val),end="")
            print()
except FileNotFoundError:
    print("File Doesn't Exist!")
    print("-------------------------------------")

# Another example of Reading the data as Dict reader
import csv

try:
    with open("noor.csv","r") as fp:
        csvdr = csv.DictReader(fp)
        for record in csvdr:
            for name,val in record.items():
                print("\t\t{}---->{}".format(name, val))
            print()
except FileNotFoundError:
    print("File Doesn't Exist!")
    print("-------------------------------------")