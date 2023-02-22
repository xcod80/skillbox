import random
def strike():
    left = random.randint(1, len(stick_list))
    right = random.randint(1, len(stick_list))
    if left > right:
        return right, left
    else:
        return left, right
stick_list = "|" * int(input("Количество палок: "))
for i in range(int(input("Количество бросков: "))):
    left_i, right_i = strike()
    stick_list = stick_list[:left_i - 1] + "." * (right_i - left_i + 1) + stick_list[right_i:]
    print("Бросок", i, ". Сбиты палки с номера", left_i, "по номер", right_i, ".")

print("Результат:", stick_list)
