import sqlite3

con = sqlite3.connect("cgi-bin/software_database.db")
cursor = con.cursor()

def create_developers_table():
    cursor.execute("""
        CREATE TABLE Developers (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL
        )
    """)

def add_default_developer():
    cursor.execute('INSERT INTO Developers (Name) VALUES (?)', ('Земля',))

create_developers_table()
add_default_developer()

con.commit()
con.close()