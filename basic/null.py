import sqlite3

conn = sqlite3.connect("template1.db")
cursor = conn.cursor()

cursor.execute("""
    SELECT *
    FROM vehicles
    WHERE year IS NULL
""")

for row in cursor.fetchall():
    print(row)

conn.close()