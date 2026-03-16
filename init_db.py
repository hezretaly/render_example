import sqlite3

conn = sqlite3.connect("database.db")
c = conn.cursor()

c.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")

c.execute("""
CREATE TABLE items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
)
""")

c.execute("INSERT INTO users (username,password) VALUES ('admin','password')")

items = ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"]

for item in items:
    c.execute("INSERT INTO items (name) VALUES (?)", (item,))

conn.commit()
conn.close()

print("Database created")