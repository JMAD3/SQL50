import sqlite3

conn = sqlite3.connect("template1.db")
cursor = conn.cursor()

cursor.execute("""
    SELECT *
    FROM vehicles
    WHERE year = 1979 AND model = 'Ford'
""")

for row in cursor.fetchall():
    print(row)

cursor.execute("""
    SELECT *
    FROM vehicles
    WHERE model = 'Ford' OR year IS NULL 
""")

for row in cursor.fetchall():
    print(row)

cursor.execute("""
    SELECT *
    FROM vehicles
    WHERE year IS NOT NULL             
""")

for row in cursor.fetchall():
    print(row)

conn.close()