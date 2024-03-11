№1

def prost(number):
  result = 0
  for i in range(2, number):
    if number % i == 0:
      return False
  return True
  
def sum_prost(number):
  result = 0
  for i in range(2, number):
    if number % i == 0 and prost(i):
      result += i
  return result
  
def kol_nechet(number):
  result = 0
  while number > 0:
    digit = number % 10
    if digit > 3 and digit % 2 != 0:
        result += 1
    number //= 10
  return result
  
def proizv(number):
  result = 1
  while number > 0:
    result *= number % 10
    number //= 10
  return result
  
print(sum_prost(int(input('Введите число для 1-й функции: '))))
print(kol_nechet(int(input('Введите число для 2-й функции: '))))
print(proizv(int(input('Введите числодля 3-й функции: '))))
