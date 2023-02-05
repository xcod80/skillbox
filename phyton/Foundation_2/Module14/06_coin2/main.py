# TODO здесь писать код

while True:
    try:
        x, y, r = float(input("x: ")), float(input("y: ")), float(input("Введите радиус: "))
    except Exception:
        print("Необходимо вводить числа!!!")
    else:
        break

if (x**2 + y**2) <= r ** 2:
    print("Монетка где-то рядом")
else:
    print("Монетки в области нет")
