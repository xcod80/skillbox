def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number%i == 0:
            return False
    else:
        return True

def crypto(data):
    return [unit[1] for unit in enumerate(data) if is_prime(unit[0])]


print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))