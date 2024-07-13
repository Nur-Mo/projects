import mysql.connector

try:
    con = mysql.connector.connect(host="localhost",
                                  user="root",
                                  passwd="root",
                                  database="collage")
    cur = con.cursor()

    # Create the students table if it doesn't exist
    tq = "CREATE TABLE IF NOT EXISTS students (eno INT PRIMARY KEY, name VARCHAR(50) NOT NULL, marks FLOAT NOT NULL, cname VARCHAR(50) NOT NULL)"
    cur.execute(tq)
    print("Table Created in MySQL, verify----")

    # Fetch column names from the students table
    cur.execute("SHOW COLUMNS FROM students")
    columns = [column[0] for column in cur.fetchall()]

    # Prompt user to input data for each column
    values = []
    for column in columns:
        value = input(f"Enter value for {column}: ")
        values.append(value)

    # Construct the INSERT INTO query dynamically
    insert_query = "INSERT INTO students (" + ", ".join(columns) + ") VALUES (" + ", ".join(["%s"] * len(columns)) + ")"
    cur.execute(insert_query, tuple(values))
    con.commit()  # Committing the transaction

    print("Data inserted into students table Successfully")

except mysql.connector.Error as err:
    print("Problem in MySQL Database:The Number you have Entered does Exist please Try Again!", err)

finally:
    cur.close()  # Closing cursor
    con.close()  # Closing connection
