numbers = ['Первый', 'Второй', 'Третий', 'Четвертый', 'Пятый', 'Шестой', 'Седьмой', 'Восьмой', 'Девятый']
PizzaTime_contrcts = dict()
for i in range(int(input('Введите количество заказов: '))):
    contract = input(f'{numbers[i]} заказ: ').title().split()
    if PizzaTime_contrcts.get(contract[0]) == None:
        PizzaTime_contrcts[contract[0]] = {contract[1]:int(contract[2])}
    else:
        PizzaTime_contrcts[contract[0]][contract[1]] = PizzaTime_contrcts[contract[0]].get(contract[1], 0) + int(contract[2])
for name in PizzaTime_contrcts:
    print('{}:'.format(name))
    for pizza in PizzaTime_contrcts[name].items():
        print('\t{}: {}'.format(pizza[0], pizza[1]))
