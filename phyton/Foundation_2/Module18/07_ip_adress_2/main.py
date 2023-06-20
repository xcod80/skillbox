addres = input("Введите IP: ").split('.')
if len(addres) != 4:
    print("Адрес — это четыре числа, разделённые точками.")
else:
    for digit in addres:
        if not digit.isdigit():
            print(digit, "— это не целое число.")
            break
        elif int(digit) > 255:
            print(digit, "превышает 255.")
            break
    else:
        print("IP-адрес корректен.")

