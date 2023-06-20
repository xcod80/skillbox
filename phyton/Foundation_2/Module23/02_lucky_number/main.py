import io
import random
sum = 0
with open('out_file.txt', 'w') as output_file:
    while sum < 777:
        try:
            number = int(input('Введите число: '))
            sum += number
            print(f'{number}', file=output_file)
            if random.randint(1, 13) == 13:
                raise Exception
        except io.UnsupportedOperation:
            print('Ошибка записи в файл: out_file.txt')
        except ValueError:
            print('Необходимо вводить целое число!')
        except Exception:
            print('Вас постигла неудача!!!')
            exit(0)
print('Вы успешно выполнили условие для выхода из порочного цикла!')
