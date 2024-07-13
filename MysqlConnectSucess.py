import mysql.connector
try:
    con = mysql.connector.connect(host="localhost",
                                  user="root",
                                  passwd="root")
    print("Python Prog got connection from MYSQL")
    cur = con.cursor()
    print("Python Program Create cursor Object")
except mysql.connector.DatabaseError as db:
    print("Problem in Mysql Database:",db)