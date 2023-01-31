print('Задача 3. Апгрейд калькулятора')

# Степан, как и большая часть населения планеты,
# для расчёта суммы и разности чисел использует калькулятор.
# 
# Однако в работе ему нужно
# делать не только  обычные действия вроде сложения и вычитания,
# а делать что-то вручную он уже устал.
# 
# Поэтому Степан решил немного расширить функциональность своего калькулятора.
# 
# Напишите программу,
# которая спрашивает у пользователя число и действие, 
# которое нужно с ним сделать: 
# вывести сумму его цифр,
# вывести максимальную цифру или вывести минимальную цифру. 
# 
# Каждое действие оформите в виде отдельной функции, 
# а основную программу зациклите.

def sum_n(number):
  S_num = 0
  for N in str(abs(number)):
    S_num += int(N)
  print('Сумма цифр числа:', S_num)

def max_n(number):
  max_number = int(str(abs(number))[0])
  for N in str(abs(number)):
    if int(N) > max_number:
      max_number = int(N)
  print('Максимальная цифра числа:', max_number)

def min_n(number):
  min_number = int(str(abs(number))[0])
  for N in str(abs(number)):
    if int(N) < min_number:
      min_number = int(N)
  print('Минимальная цифра числа:', min_number)

def main():
  number = int(input('Введите число: '))
  print('1 - Сумма цифр')
  print('2 - Вывести максимальную цифру')
  print('3 - Вывести минимальную цифру')
  choice = int(input('Выберите действие: '))
  if choice == 1:
    sum_n(number)
  elif choice == 2:
    max_n(number)
  elif choice == 3:
    min_n(number)
  else:
    print('Ошибка выбора!!!')
  main()

main()