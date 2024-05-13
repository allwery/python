import sqlite3

conn = sqlite3.connect('space.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE Planets (
                    ID INTEGER PRIMARY KEY,
                    Name TEXT,
                 )''')

cursor.execute('''CREATE TABLE Parameters (
                    ID INTEGER PRIMARY KEY,
                    Planet_ID INTEGER,
                    Mass REAL,
                    Diameter REAL,
                    FOREIGN KEY (Planet_ID) REFERENCES Planets(ID)
                 )''')

cursor.execute('''CREATE TABLE Satellites (
                    ID INTEGER PRIMARY KEY,
                    Name TEXT,
                    Planet_ID INTEGER,
                    FOREIGN KEY (Planet_ID) REFERENCES Planets(ID)
                 )''')

cursor.execute("INSERT INTO Planets (Name) VALUES ('Mercury')")
cursor.execute("INSERT INTO Planets (Name) VALUES ('Venus')")
cursor.execute("INSERT INTO Planets (Name) VALUES ('Earth')")

mercury_id = cursor.lastrowid
venus_id = cursor.lastrowid
earth_id = cursor.lastrowid

cursor.execute(f"INSERT INTO MassAndDiameter (Planet_ID, Mass, Diameter) VALUES ({mercury_id}, 0.03, 4879)")
cursor.execute(f"INSERT INTO MassAndDiameter (Planet_ID, Mass, Diameter) VALUES ({venus_id}, 0.48, 12104)")
cursor.execute(f"INSERT INTO MassAndDiameter (Planet_ID, Mass, Diameter) VALUES ({earth_id}, 5.97, 12742)")


cursor.execute("INSERT INTO Satellites (Name, Planet_ID) VALUES ('None', {mercury_id}")
cursor.execute("INSERT INTO Satellites (Name, Planet_ID) VALUES ('Neit', {venus_id}")
cursor.execute("INSERT INTO Satellites (Name, Planet_ID) VALUES ('Moon', {earth_id}")

conn.commit()
conn.close()
