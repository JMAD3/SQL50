import sqlite3

conn = sqlite3.connect("template1.db")
cursor = conn.cursor()

cursor.execute("""
    SELECT *
    FROM vehicles
    ORDER BY id DESC
""")

for row in cursor.fetchall():
    print(row)

cursor.execute("""
    SELECT *
    FROM vehicles
    ORDER BY year, model
""")

for row in cursor.fetchall():
    print(row)

conn.close()
