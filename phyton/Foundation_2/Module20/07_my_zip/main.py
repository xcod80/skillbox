my_string = 'abcd'
my_tuple = (10, 20, 30, 40)
my_list = [4, 5, 6]

def my_zip(*args):
    return (tuple([args[j][i] for j in range(len(args))]) for i in range(min((len(args[k]) for k in range(len(args))))))

print('Встроенная функция zip')
print(zip(my_string, my_tuple))
for val in zip(my_string, my_tuple):
    print(val)
print()

print('Мой вариант функции zip')
print(my_zip(my_string, my_tuple))
for val in my_zip(my_string, my_tuple, my_list):
    print(val)

