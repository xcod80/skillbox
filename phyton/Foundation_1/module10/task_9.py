print('Задача 9. Пирамидка 2')


# Напишите программу,
# которая получает на вход количество уровней пирамиды и выводит их на экран,

# Пример:
# 
#             1
#          3     5
#       7     9     11
#    13    15    17    19
# 21    23    25    27    29

height = int(input('Введите высоту пирамиды: '))
num = 1

for y in range(1, height + 1):
  '''for x in range(height - y):
    print('\t', end = '')'''
  print('\t' * (height - y), end = '')
  for x in range(y):
    print(num, end = '\t\t')
    num += 2
  print()
