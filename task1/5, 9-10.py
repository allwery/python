№5
#Необходимо найти все даты, которые описаны в
#виде "31 февраля 2007".

import re 
#Этот оператор импортирует модуль регулярных выражений re,
#который позволяет работать с регулярными выражениями.

def find_dates(text):
    pattern = r'\b\d{1,2} [а-яА-Я]+ \d{4}\b' #Это регулярное выражение (pattern), 
    #которое ищет даты со следующими особенностями:
  # - \b: Указывает на границу слова.
  # - \d{1,2}: Одна или две цифры для дня.
  # - [а-яА-Я]+: Одно или более русских букв (дополните можно нужными символами для других языков).
  # - \d{4}: Четыре цифры для года.
    dates = re.findall(pattern, text)# поиск всех подстрок в тексте, 
    #соответствующих регулярному выражению
    return dates

text = input("Введите текст: ")
dates = find_dates(text)
print("Найденные даты:", dates)

№9
#Прочитать список строк с клавиатуры. Упорядочить по длине
#строки.

def read_list():
    list = []
    while True:
        s = input()
        if s == '':
            break
        list.append(s)
    return list

def sort_list(list):
    list.sort(key=len) #метод sort() и параметр key=len, который сравнивает элементы по их длине
    return list

def print_list(list):
    for s in list:
        print(s)


def main():
    list = read_list()
    list = sort_list(list)
    print_list(list)

main()

№10
#Дан список строк с клавиатуры. Упорядочить по количеству
#слов в строке.

def count_words(sent):
  return len(sent.split())
  
n = int(input("Введите количество строк: "))
str = []
for _ in range(n):
  str.append(input("Введите строку: "))

sort_str = sorted(str, key=lambda x: count_words(x))
print("Отсортированный список строк по количеству слов:")
for string in sort_str:
  print(string)
