import sqlite3

conn = sqlite3.connect("template1.db")
cursor = conn.cursor()

print("Limit vairable (cap at 3)")

cursor.execute("""
    SELECT *
    FROM vehicles
    LIMIT 3
""")

for row in cursor.fetchall():
    print(row)


cursor.execute("""
    SELECT *
    FROM vehicles
    WHERE year > 1950
""")

print("Where clause, apply operators to poperties")

for row in cursor.fetchall():
    print(row)

print("GROUP BY only fetches data from specific groups")

cursor.execute("""
    SELECT year,
    COUNT(*)
    FROM vehicles
    GROUP BY year 
""")

for row in cursor.fetchall():
    print(row)

conn.close()