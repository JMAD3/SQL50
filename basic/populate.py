import sqlite3

def main():
  populate()
  printTables()
    

def populate():
    
  conn = sqlite3.connect("template1.db")
  cursor = conn.cursor()

  cursor.execute("""
      CREATE TABLE IF NOT EXISTS vehicles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT,
        year INTEGER
      )
  """)

  cursor.execute("INSERT INTO vehicles (model, year) VALUES (?,?)", ("Ford", 1979))

  cursor.execute("INSERT INTO vehicles (model, year) VALUES (?,?)", ("", None))
  
  conn.commit()
  conn.close()

def printTables():

  conn = sqlite3.connect("template1.db")
  cursor = conn.cursor()
  
  cursor.execute("SELECT * FROM vehicles")
  for row in cursor.fetchall():
    print(row)

  conn.close()

main()