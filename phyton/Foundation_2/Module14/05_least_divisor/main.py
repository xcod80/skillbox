# TODO здесь писать код

while True:
    try:
        number = int(input("Введите число:"))
    except Exception:
        print("Введите целое число!!!\n")
    else:
        break
divider = 2
while (number % divider) != 0:
    divider += 1
print("Наименьший делитель, отличный от единицы:", divider)
