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
    print(f"<div>Ошибка при добавлении галактики: {e}</div>")
else:
    print("<div>Галактика добавлена!</div>")
finally:
    con.close()
    print("<a href=\"../index.html\">Назад</a>")
    print()
    print("</html>")