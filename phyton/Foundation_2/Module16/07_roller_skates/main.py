list_skates = []
list_legssize = []
number = int(input("Кол-во коньков: "))
for i in range(number):
    list_skates.append(int(input(f'Размер {i+1}-й пары:')))
number = int(input("Кол-во людей: "))
for i in range(number):
    list_legssize.append(int(input(f'Размер ноги {i+1}-го человека :')))
number = 0
for legsize in list_legssize:
    if legsize in list_skates:
        number +=1
        list_skates.remove(legsize)
print("Наибольшее кол-во людей, которые могут взять ролики:", number)