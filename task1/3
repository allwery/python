1.1 Дана строка. Необходимо найти максимальное из имеющихся в ней
вещественных чисел.
def max_number(string):
    max_num = 0
    for i in string.split():
        if float(i) > max_num:
            max_num = float(i)
    return max_num
string = input('Введите строку: ')
print(max_number(string))

1.9 Дана строка. Необходимо найти минимальное из имеющихся в ней
рациональных чисел.

1.18
def find_max_sequence(string):
  max_length = 0
  current_length = 0
  for i in string:
    if i.isdigit():
        current_length += 1
    else:
        if current_length > max_length:
          max_length = current_length
        current_length = 0
  if current_length > max_length:
    max_length = current_length
  return max_length

string = input("Введите строку: ")
print(find_max_sequence(string))
