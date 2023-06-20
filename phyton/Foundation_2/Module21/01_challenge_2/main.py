def nums(number):
    if number == 0:
        return number
    else:
        nums(number - 1)
    print(number)
    return

num = int(input('Введите num: '))
nums(num)
