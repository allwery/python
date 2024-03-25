#Отсортировать строки в указанном порядке
 #В порядке увеличения разницы между количеством согласных и
#количеством гласных букв в строке.

def count_vowels(s):
  return sum(1 for c in s if c in 'aeiouAEIOU')

def count_consonants(s):
  return len(s) - count_vowels(s)

def compare(s1, s2):
  return count_consonants(s1) - count_consonants(s2)

def sort_strings(strings):
  return sorted(strings, key=lambda s: (count_consonants(s), -count_vowels(s)))

strings = input("Введите строки через пробел: ").split()
sorted_strings = sort_strings(strings)
print(sorted_strings)



#Отсортировать строки в указанном порядке
# В порядке увеличения разницы между количеством сочетаний
#«гласная-согласная» и «согласная-гласная» в строке

def count_vow_con(s):
  vow = "aeiouAEIOU"
  con = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
  vow_con = sum([1 for i in range(len(s) - 1) if s[i] in vow and s[i+1] in con]) - sum([1 for i in range(len(s) - 1) if s[i] in con and s[i+1] in vow])
  return vow_con

def sort_strings(strings):
  return sorted(strings, key=lambda s: count_vow_con(s))

strings = input("Введите строку: ").split()
sorted_strings = sort_strings(strings)
print(sorted_strings)



#Отсортировать строки в указанном порядке
#В порядке увеличения среднего количества «зеркальных» троек
#(например, «ada») символов в строке

def count_mirror(s):
  count = 0
  for i in range(len(s) - 2):  # Проходим по строке за исключением двух последних символов
      if s[i] == s[i+2] and s[i] != s[i+1]:  # Проверяем, что символы составляют зеркальную тройку
          count += 1
  return count

def sort_triples(strings):
  return sorted(strings, key=lambda s: count_mirror(s))

strings = input("Введите строку: ").split()
sorted_strings = sort_triples(strings)
print(sorted_strings)
