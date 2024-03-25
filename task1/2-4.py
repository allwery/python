В1 Задачи 1, 9, 18

1. Дана строка. Необходимо найти общее количество русских символов.

def count_russian(string):
  russian_chars = "абвгдеёжзиклмнопрстуфхцчшщъыьэюя"
  count = sum( 1 for char in string if char in russian_chars)
  return count
string=input('Введите символы: ')
russian_count=count_russian(string)
print(russian_count)




9. Дана строка. Необходимо проверить образуют ли строчные символы
латиницы палиндром. 
Ошибка в регистре и не различает латиницу с кир.

def palindrom(string):
   if string == string[::-1]:
       return True
   else:
       return False
string = input('Введите строку: ')
print(palindrom(string))

18. Найти в тексте даты формата «день.месяц.год».

///
