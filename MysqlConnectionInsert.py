import mysql.connector

try:
    con = mysql.connector.connect(host="localhost",
                                  user="root",
                                  passwd="root",
                                  database="school")
    cur = con.cursor()

    # Create the students table if it doesn't exist
    tq = "CREATE TABLE IF NOT EXISTS student (eno INT PRIMARY KEY, name VARCHAR(50) NOT NULL, salary FLOAT NOT NULL, cname VARCHAR(50) NOT NULL)"
    cur.execute(tq)
    print("Table Created in MySQL, verify----")

    # Fetch column names from the students table
    cur.execute("SHOW COLUMNS FROM student")
    columns = [column[0] for column in cur.fetchall()]

    # Prompt user to input data for each column
    values = []
    for column in columns:
        value = input(f"Enter value for {column}: ")
        values.append(value)

    # Construct the INSERT INTO query dynamically
    insert_query = "INSERT INTO student (" + ", ".join(columns) + ") VALUES (" + ", ".join(["%s"] * len(columns)) + ")"
    cur.execute(insert_query, tuple(values))
    con.commit()  # Committing the transaction

    print("Data inserted into student table Successfully")

except mysql.connector.Error as err:
    print("Problem in MySQL Database,The number you have entered does Exist please try again:", err)

finally:
    cur.close()  # Closing cursor
    con.close()  # Closing connection
