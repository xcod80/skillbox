import re
numbers_list = ['7999999999', '9999999999', '999999-999', '99999x9999']

for number in numbers_list:
    if re.fullmatch(r'[89]\d{9}', number):
        print(f'Номер {number}: все в порядке')
    else:
        print(f'Номер {number}: не подходит')