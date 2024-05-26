import cgi
import sqlite3

con = sqlite3.connect("cgi-bin/software_database.db")
cursor = con.cursor()
form = cgi.FieldStorage()
title = form.getfirst("title")
version = form.getfirst("version")
developer = form.getfirst("developer")
description = form.getfirst("description")

print("Content-type: text/html\n")  # Добавлен заголовок Content-type для правильной работы CGI

print("<html>")
print()
print("<head><meta charset=\"UTF-8\"></head>")
try:
    cursor.execute('INSERT INTO Bilet (Title, Price, Planeta, Description) VALUES (?, ?, ?, ?)',
                   (title, version, developer, description))
    con.commit()
except Exception as e:
    print(f"<div>Oshibka pri oformlenii bileta: {e}</div>")
else:
    print("<div>Bilet uspeshno dobavlen!</div>")
finally:
    con.close()
    print("<a href=\"../index.html\">Nazad</a>")
    print()
    print("</html>")