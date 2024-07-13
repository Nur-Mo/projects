import mysql.connector
try:
    con = mysql.connector.connect(host="localhost",
                                  user="root",
                                  passwd="root")
    print("Python Prog got connection from MYSQL")
except mysql.connector.DatabaseError as db:
    print("Problem in Mysql Database:",db)