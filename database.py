import sqlite3

conn = sqlite3.connect("ration.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS cardholders(
    card_no TEXT PRIMARY KEY,
    name TEXT,
    members INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS products(
    product_name TEXT,
    quantity INTEGER,
    price REAL
)
""")

conn.commit()
conn.close()

print("Database Created Successfully")