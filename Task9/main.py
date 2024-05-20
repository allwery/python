import csv

# Загрузить данные из CSV-файла
with open("1 - 2.csv", "r", encoding="UTF-8") as f:
    reader = csv.reader(f)
    data = list(reader)

# Получить заданную букву и дату
letter = input("Введите букву: ")
date = input("Введите дату : ")

# Найти количество людей, фамилии которых начинаются с заданной буквы и которые прошли тест раньше заданной даты
count = 0
for row in data[1:]:
    if row[0][0] == letter and row[6] < date:
        count += 1

# Вывести список людей
print(f"Количество людей, фамилии которых начинаются с буквы {letter} и которые прошли тест раньше {date}: {count}")
for row in data[1:]:
    if row[0][0] == letter and row[6] < date:
        print(row[0], row[1], row[6])