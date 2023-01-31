print('Задача 7. Наибольшая сумма цифр')

# Вводится N чисел. 
# Среди натуральных чисел, которые были введены, 
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.

N = int(input('Введите количество чисел: '))
num_list = []

for i in range(N):
  num_list.append(int(input(f'Введите число №{i + 1}: ')))
max_sum = 0
for num in num_list:
  sum = 0
  for i in range(len(str(num))):
    sum += num % 10
  if sum > max_sum:
    max_sum = sum
    max_num = num
print(f'В данной последовательности максимальная сумма цифр {max_sum} в числе {max_num}')