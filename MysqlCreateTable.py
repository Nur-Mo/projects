import mysql.connector

try:
    con = mysql.connector.connect(host="localhost",
                                  user="root",
                                  passwd="root",
                                  database="school")
    cur = con.cursor()
    tq = "CREATE TABLE students (eno INT PRIMARY KEY, name VARCHAR(10) NOT NULL, marks REAL NOT NULL, cname VARCHAR(10) NOT NULL)"  # Added space between field names and data types

    cur.execute(tq)
    print("Table Created in MySQL, verify----")

except mysql.connector.Error as err:
    print("Problem in MySQL Database:", err)
