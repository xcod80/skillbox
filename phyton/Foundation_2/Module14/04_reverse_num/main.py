# TODO здесь писать код

def revert_number(number):
    number_int = int(str(number).split('.')[0][::-1])
    number_div = int(str(number).split('.')[1][::-1]) / (10 ** len(str(number).split('.')[1]))
    return number_int + number_div

while True:
    try:
        N, K = float(input("Введите первое число: ")), float(input("Введите второе число: "))
    except Exception:
        print("Необходимо вводить вещественные числа с разделителем '.'!!!")
    else:
        break

print("Первое число наоборот:", revert_number(N))
print("Первое второе наоборот:", revert_number(K))
print("Сумма:", revert_number(N) + revert_number(K))