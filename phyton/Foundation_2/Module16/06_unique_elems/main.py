list_1, list_2 = [], []
for i in range(1,4):
    list_1.append(int(input(f'Ведите {i}-е число для первого списка:')))
for i in range(1,8):
    list_2.append(int(input(f'Ведите {i}-е число для второго списка:')))
print("Первый список:", list_1)
print("Второй список:", list_2)
list_1.extend(list_2)
for elem in list_1:
    while list_1.count(elem)>1:
        list_1.remove(elem)
print("Новый первый список с уникальными элементами: ",list_1)