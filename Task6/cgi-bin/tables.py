import sqlite3
import sys

def create_database_tables():
    con = sqlite3.connect("cgi-bin/software_database.db")
    cursor = con.cursor()

    # Создание таблицы Software
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Bilet (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Title TEXT NOT NULL,
            Age TEXT NOT NULL,
            Planeta TEXT NOT NULL,
            Description TEXT
        )
    """)

    # Создание таблицы Releases
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Polet (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            PlanetaID INTEGER NOT NULL,
            ReleaseDate TEXT NOT NULL,
            FOREIGN KEY (PlanetaID) REFERENCES Bilet(ID)
        )
    """)

    # Создание таблицы Developers
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Planeta (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL
        )
    """)

    con.commit()
    con.close()

def select_data_from_tables():
    con = sqlite3.connect("cgi-bin/software_database.db")
    cursor = con.cursor()

    cursor.execute("SELECT * FROM Bilet")
    software = cursor.fetchall()

    cursor.execute("SELECT * FROM Polet")
    releases = cursor.fetchall()

    cursor.execute("SELECT * FROM Planeta")
    developers = cursor.fetchall()

    con.close()

    return software, releases, developers

def main():
    create_database_tables()
    software, releases, developers = select_data_from_tables()

    sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='cp1251', buffering=1)

    print("Content-type: text/html\n")  # Добавлен заголовок Content-type для правильной работы CGI

    print("<html>")
    print("<head>")
    print("<meta charset=\"windows-1251\">")
    print("<link rel=\"stylesheet\" href=\"../style.css\">")
    print("<title>Таблицы</title>")
    print("<style>")
    print("body {")
    print("    background-color: white; /* Кремовый цвет заднего фона сайта */")
    print("    font-family: 'Times New Roman', Times, serif;")  # изменение шрифта
    print("    color: black; /* Нежно розовый цвет текста */")
    print("    text-align: center;")  # Центрирование текста по центру страницы
    print("    margin: 0;")  # Убираем отступы
    print("}")
    print("table {")
    print("    text-align: center;")
    print("    width: 80%;")  # Уменьшение ширины таблиц
    print("    margin: 20px ;")  # Центрирование таблиц на странице
    print("    margin-left: -500px ;")
    print("    border-collapse: collapse;")
    print("    background-color: #fff; /* Белый цвет фона таблиц */")
    print("}")
    print("tn{")

    print("    text-align: center;")
    print("}")
    print("th, td {")
    print("    border: 1px solid  #white;")
    print("    padding: 10px;")
    print("    text-align: left;")
    print("}")
    print("th {")
    print("    background-color: #fff; /* Нежно розовый цвет фона заголовков столбцов */")
    print("    color: black; /* Белый цвет текста заголовков столбцов */")
    print("}")
    print("tr:nth-child(even) {")
    print("    background-color: #fff; /* Цвет фона четных строк */")
    print("}")
    print(".flex-div {")
    print("    display: flex;")
    print("    justify-content: space-between;")
    print("    margin-top: 20px;")
    print("}")
    print("</style>")
    print("</head>")
    print("<body>")
    print("<div style=\"padding: 20px;\">")
    print("<h1>Данные о полетах</h1>")
    print("<div class=\"flex-div\">")
    print("<table>")
    print("<div class=\"flex-div\"><table><tr><tn colspan=\"0\">Билет</tn></tr><tr><th>ID</th><th>ФИО</th><th>Возраст</th><th>Планета</th><th></th></tr>")
    for software_row in software:
        print(
            f"<tr><td>{software_row[0]}</td><td>{software_row[1]}</td><td>{software_row[2]}</td><td>{software_row[3]}</td></tr>")
    print("</table>")
    print("</div>")
    print("<div class=\"flex-div\">")
    print("<table>")
    print("<table><tr><tn colspan=\"0\">Полет</tn></tr><tr><th>Планета ID</th><th>Дата полета</th></tr>")
    for release_row in releases:
        print(f"<tr><td>{release_row[1]}</td><td>{release_row[2]}</td></tr>")
    print("</table>")
    print("</div>")
    print("<div class=\"flex-div\">")
    print("<table>")
    print("<table><tr><tn colspan=\"0\">Планета</tn></tr><tr><th>ID</th><th>Галактика</th></tr>")
    for developer_row in developers:
        print(f"<tr><td>{developer_row[0]}</td><td>{developer_row[1]}</td></tr>")
    print("</table>")
    print("</div>")
    print("</div>")
    print("</body>")
    print("<div class=\"flex-div\"><a href=\"../index.html\">Назад</a></div>")
    print("</html>")


if __name__ == "__main__":
    main()