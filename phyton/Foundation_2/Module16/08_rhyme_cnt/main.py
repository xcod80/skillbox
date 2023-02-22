list_mans = list(range(1,int(input("Кол-во человек: "))+1))
num = int(input("Какое число в считалке? "))
man = list_mans[0]
print(f'Значит выбывает каждый {num}-й человек')

while len(list_mans) > 1:
    print("Текущий круг людей: ", list_mans)
    print("Начало счета с номера", man)
    last_man = man
    man = list_mans[(num + list_mans.index(last_man))%len(list_mans)]
    print("Выбывает человек под номером", list_mans.pop((num + list_mans.index(last_man) - 1)%len(list_mans)))
    print()
print("Остался человек под номером", list_mans[0])
