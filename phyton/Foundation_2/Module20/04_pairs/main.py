#Вариант 1

input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print('Оригинальлный список: ', input_list)
new_list = list(zip(input_list[::2], input_list[1::2]))
print('Новый список:', new_list)


#Вариант 2
input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print('Оригинальлный список: ', input_list)
new_list = [tuple([input_list[i],input_list[i + 1]]) for i in range(0, 10, 2)]
print('Новый список:', new_list)
