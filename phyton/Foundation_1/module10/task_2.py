print('Задача 2. Лестница')

# Пользователь вводит число N.
# Напишите программу, которая выводит такую “лесенку” из чисел:

# Введите число: 5
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

num = int(input('Введите число: '))

for cur_num in range(1, num + 1):
  for print_num in range(cur_num):
    print(cur_num, end = ' ')
  print()

#Вариант с одним циклом

num = int(input('Введите число: '))

for cur_num in range(1, num + 1):
  print((str(cur_num) + ' ') * cur_num)

