import mysql.connector
try:
    con = mysql.connector.connect(host="localhost",
                                  user="root",
                                  passwd="root")
    cur = con.cursor()
    dc = "Create database School" #This is where we create or use (Drop) the table
    cur.execute(dc)
    print("Database Create in MYSQL")
except mysql.connector.DatabaseError as db:
    print("Problem in MYSQL Database")


