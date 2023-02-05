# TODO здесь писать код

def number_len(num):
    return len(num)

def number_sum(num):
    summa = 0
    for symbol in num:
        summa += int(symbol)
    return summa

while True:
    number = input("\nВведите число: ")
    if number.isdigit():
        break
    else:
        print("Нужно вводить только цифры!!!!\n")

print("Сумма цифр числа:", number_sum(number))
print("Количество цифр числа: ", number_len(number))
