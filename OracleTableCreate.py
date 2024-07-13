#Prog for creating employee table
import oracledb as orc
try:
    orc.init_oracle_client()
    con = orc.connect("system/manager@localhost/xe")
    cur = con.cursor()

    tc = input("Enter Query to create a table on Oracle DB: ")
    cur.execute(tc)

    print("Table Created in Oracle Database --- verify")
except orc.DatabaseError as db:
    print("Problem on Oracle DB",db)

