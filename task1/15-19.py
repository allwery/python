#1.Необходимо найти количество элементов,
#расположенных после последнего максимального.

def find_max(arr):
  max_val = arr[0]
  max_index = 0
  for i in range(1, len(arr)):
    if arr[i] > max_val:
      max_val = arr[i]
      max_index = i
  return max_index

def count_after_max(arr):
  max_index = find_max(arr)
  count = 0
  for i in range(max_index + 1, len(arr)):
    count += 1
  return count

arr = [int(x) for x in input().split()] # Это генератор списка, который преобразует каждую подстроку, 
print(count_after_max(arr))             #полученную из ввода, в целое число и добавляет это целое число в новый список.


#13.Дан целочисленный массив и интервал a..b. Необходимо найти
количество элементов в этом интервале.

def main():
  a = int(input("Введите число a: "))
  b = int(input("Введите число b: "))
  array = []
  for i in range(a, b+1):
    array.append(i) #каждое значение i добавляется в список array с помощью метода append()
  print(len(array))

if __name__ == "__main__": #После определения функции main(), идет проверка на то, 
  main()                    #что если имя модуля (__name__) равно строке "__main__", 
                            #тогда вызывается функция main().



#25.ан целочисленный массив и интервал a..b. Необходимо найти
#максимальный из элементов в этом интервале

def max_in_interval(a, b):
  max_num = a
  for i in range(a, b+1):
    if i > max_num:
      max_num = i
  return max_num

a = int(input("Введите начало интервала: "))
b = int(input("Введите конец интервала: "))
print(max_in_interval(a, b))


#37.Дан целочисленный массив. Вывести индексы элементов, которые
#меньше своего левого соседа, и количество таких чисел.
def main():
  arr = [int(i) for i in input().split()]
  count = 0
  for i in range(1, len(arr) ):
    if arr[i] < arr[i - 1]:
      count += 1
      print(i, end = ' ')
  print()
  print(count)

if __name__ == '__main__':
  main()


