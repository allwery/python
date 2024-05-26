import cgi
import sqlite3

con = sqlite3.connect("cgi-bin/software_database.db")
cursor = con.cursor()
form = cgi.FieldStorage()
name = form.getfirst("name")

print("Content-type: text/html\n")  # Добавлен заголовок Content-type для правильной работы CGI

print("<html>")
print()
print("<head><meta charset=\"UTF-8\"></head>")
try:
    cursor.execute('INSERT INTO Planeta (Name) VALUES (?)', (name,))
    con.commit()
except Exception as e:
    print(f"<div>Oshibka pri dobavlenii galaktiki: {e}</div>")
else:
    print("<div>Galaktika dobavlena!</div>")
finally:
    con.close()
    print("<a href=\"../index.html\">Nazad</a>")
    print()
    print("</html>")