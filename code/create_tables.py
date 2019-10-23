import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_tables = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_tables)

create_tables = "CREATE TABLE IF NOT EXISTS items (name text, price real)"
cursor.execute(create_tables)

connection.commit()
connection.close()