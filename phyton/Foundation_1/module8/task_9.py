print('Задача 9. Выражение')


#Дано число x.
#Напишите программу для вычисления следующего выражения 

# ((x-1)(x-3)(x-7)…(x-63)/
# ((x-2)(x-4)(x-8)…(x-64))

x = float(input('Введите значение x: '))
numerator = 1
divider = 1

for n in range(1, 64, 2):
  numerator *= x - n
  divider *= x - (n+1)

if divider!=0:
  print(f'res={round(numerator/divider, 4)}')
else:
  print('res равняется бесконечно малому числу')
