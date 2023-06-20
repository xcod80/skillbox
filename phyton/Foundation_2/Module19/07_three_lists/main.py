array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

print('Задача 1')
print('Решение без множеств: ', end='')
iter_array = []
[iter_array.append(item) for item in array_1 + array_2 + array_3 if item in array_1 and item in array_2 and item in array_3 and (item not in iter_array)]
for iter in iter_array:
    print(iter, end=' ')
print()
print('Решение с множествами: ', end='')
iter_set = set(array_1) & set(array_2) & set(array_3)
for iter in iter_set:
    print(iter, end=' ')
print('\n\n')
print('Задача 2')
print('Решение без множеств: ', end='')
iter_array = [item for item in array_1 if item not in array_2 and item not in array_3]
for iter in iter_array:
    print(iter, end=' ')
print()
print('Решение с множествами: ', end='')
iter_set = set(array_1).difference(array_2, array_3)
for iter in iter_set:
    print(iter, end=' ')
print('\n\n')

print()