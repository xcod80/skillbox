text_list = list(input('Введите строку: ').lower())

for symbol in text_list:
    if text_list.count(symbol) >= 2:
        text_list.remove(symbol)
        text_list.remove(symbol)
if len(text_list) > 1:
    print('Нельзя сделать палиндром')
else:
    print('Можно сделать палиндром')
