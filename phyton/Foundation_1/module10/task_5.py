print('Задача 5. Простые числа')


#Напишите программу,
#которая считает количество простых чисел в заданной последовательности 
#и выводит ответ на экран.

num_count = int(input('Введите количество чисел: '))
list_nums = []
for i in range(num_count):
  list_nums.append(int(input('Введите число: ')))
not_prime = 0
for num in list_nums:
  if num > 1:
    for divider in range(2, num):
      if (num // divider) > 0 and (num % divider) == 0:
        not_prime += 1
        break
  else:
    not_prime += 1
print('Количество простых чисел в последовательности: ', num_count - not_prime)