print('Задача 8. Сумма ряда')

# Пользователь вводит действительное число
# "х" и точность "precision".

# P.S: Формулу смотреть на сайте :)


# Напишите программу,
# которая по число х вычисляет сумму ряда в точности до precision.


# Операцией возведения в степень и функцией factorial пользоваться нельзя.

# Пример:
# Введите точность: 0.001

# Введите x: 5
# Сумма ряда =  0.2836250150891709

def fact(x):
  if x <= 1:
    return 1
  else:
    return x * fact(x - 1)


x = float(input('Введите значение X: '))
precision = float(input('Введите точночть: '))
S = S_n = x_n = 1
signum = -1
index = 2
while precision <= S_n:
  x_n *= x * x
  S_n = x_n / fact(index)
  index += 2
  S += signum * S_n
  signum *= -1

print('Сумма ряда:', S)
