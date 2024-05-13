import sqlite3
import json
import xml.dom.minidom as minidom

print("<html>")
print()
print("<head><meta charset=\"UTF-8\"></head>")
try:
    con = sqlite3.connect("cgi-bin/software_database.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Software")
    software = cursor.fetchall()
    software = {"data": {item[0]: {"Title": item[1], "Version": item[2], "Developer": item[3], "Description": item[4]} for item in software}}
    cursor.execute("SELECT * FROM Licenses")
    licenses = cursor.fetchall()
    licenses = {"data": {item[0]: {"License Type": item[1], "Expiration Date": item[2], "Software ID": item[3]} for item in licenses}}
    cursor.execute("SELECT * FROM Users")
    users = cursor.fetchall()
    users = {"data": {item[0]: {"Name": item[1], "Email": item[2], "Registration Date": item[3]} for item in users}}
    table = {"Software": software, "Licenses": licenses, "Users": users}

    # Экспорт в XML
    doc = minidom.Document()
    root = doc.createElement('tables')
    doc.appendChild(root)

    for table_name, data in table.items():
        table_element = doc.createElement(table_name)
        for key, value in data['data'].items():
            row_element = doc.createElement('row')
            for field_name, field_value in value.items():
                field_element = doc.createElement(field_name)
                field_element.appendChild(doc.createTextNode(str(field_value)))
                row_element.appendChild(field_element)
            table_element.appendChild(row_element)
        root.appendChild(table_element)

    with open("data.xml", "w") as file:
        file.write(doc.toprettyxml())

    # Импорт из XML
    string = ""
    with open("data.xml", "r") as file:
        doc = minidom.parse(file)
        table_elements = doc.getElementsByTagName('tables')
        for table_element in table_elements:
            table_name = table_element.tagName
            data = {}
            rows = table_element.getElementsByTagName('row')
            for row in rows:
                row_data = {}
                for field in row.childNodes:
                    field_name = field.tagName
                    field_value = field.firstChild.nodeValue
                    row_data[field_name] = field_value
                data[row_data['ID']] = row_data
            string += f"{table_name}: {data}\n"
except Exception as e:
    print("ERROR!", e)
else:
    print(f"<div>File save!</div><div>date  : {string}</div>")
finally:
    print("<a href=\"../index.html\">Back</a>")