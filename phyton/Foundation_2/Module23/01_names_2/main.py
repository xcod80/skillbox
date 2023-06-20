import datetime


def sym_sum(text_file):
    sum = 0
    index = 0
    for line in text_file:
        index += 1
        line = line.strip()
        sum += len(line)
        try:
            if len(line) < 3:
                raise ValueError
        except ValueError:
            with open('errors.log', 'a') as log_file:
                print('Ошибка: менее трёх символов в строке №{}'.format(index))
                log_file.write('{} - Ошибка: менее трёх символов в строке №{}\n'.format(datetime.datetime.now(), index))
    return sum
try:
    with open('people.txt', 'r') as work_file:
        print(sym_sum(work_file))
except FileNotFoundError:
    print('Файл people.txt не найден.')

