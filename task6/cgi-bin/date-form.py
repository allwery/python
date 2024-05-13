import cgi
import sqlite3

con = sqlite3.connect("cgi-bin/software_database.db")
cursor = con.cursor()
form = cgi.FieldStorage()
software_id = form.getfirst("software_id")
release_date = form.getfirst("release_date")

print("Content-type: text/html\n")  # Добавлен заголовок Content-type для правильной работы CGI

print("<html>")
print()
print("<head><meta charset=\"UTF-8\"></head>")
try:
    cursor.execute('INSERT INTO Releases (SoftwareID, ReleaseDate) VALUES (?, ?)', (int(software_id), release_date))
    con.commit()
except Exception as e:
    print(f"<div>Oshibka pri zapisi k trenery: {e}</div>")
else:
    print("<div>Zapis k trenery proshla yspeshno!</div>")
finally:
    con.close()
    print("<a href=\"../index.html\">Nazad</a>")
    print()
    print("</html>")