import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()
# could the following be put into a for loop to seed the database with as many students as you want?
cur.execute("INSERT INTO users (username, fullName, pass) VALUES (?, ?)",
            ('student5', 'John O Doe', 'super!Safe!Password!')
            )
cur.execute("INSERT INTO users (username, fullName, pass) VALUES (?, ?)",
            ('student6', 'GI Doe', 'super!Safe!Password!!')
            )

connection.commit()
connection.close()