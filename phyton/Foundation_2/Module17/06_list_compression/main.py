import random
digit_list = [random.randint(0,2) for _ in range(int(input("Количество чисел в списке: ")))]
print("Список до сжатия:", digit_list)
for _ in range(digit_list.count(0)):
    del digit_list[digit_list.index(0)]
    digit_list.append(0)
if digit_list.count(0) > 0:
    digit_list = digit_list[:digit_list.index(0)]
print("Список после сжатия:", digit_list)