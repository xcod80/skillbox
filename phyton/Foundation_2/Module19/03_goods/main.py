goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}


for good in goods:
    quantity, price = 0, 0
    for unit in store[goods[good]]:
        quantity += unit['quantity']
        price += unit['quantity'] * unit['price']
    print('{0} -\t {1} штук,\t стоимость {2:_} рублей'.format(good, quantity, price).replace('_', ' '))