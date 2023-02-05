# TODO здесь писать код

while True:
    try:
        print("Введите первую точку")
        x1 = float(input('X: '))
        y1 = float(input('Y: '))
        print("\nВведите вторую точку")
        x2 = float(input('X: '))
        y2 = float(input('Y: '))
    except Exception:
        print("Вводить нужно только числа!\n")
    else:
        break
x_diff = x1 - x2
y_diff = y1 - y2
if x_diff == 0:
    equation = "x = " + str(x1)
elif y_diff == 0:
    equation = "y = " + str(y1)
else:
    k = y_diff / x_diff
    b = y2 - k * x2
    equation = "y = " + str(k) + " * x + " + str(b)

print("Уравнение прямой, проходящей через эти точки:")
print(equation)