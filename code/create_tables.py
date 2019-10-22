import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_tables = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_tables)

connection.commit()
connection.close()