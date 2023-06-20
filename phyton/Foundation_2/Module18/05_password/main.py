def nums_symbol(test_string, test_alphabet):
    num = 0
    for symbol in test_string:
        if symbol in test_alphabet:
            num += 1
    return num

while True:
    user_password = input("Придумайте пароль: ")
    if len(user_password) < 8 \
            or nums_symbol(user_password, [chr(i) for i in range(ord('0'), ord('9')+1)]) < 3\
            or nums_symbol(user_password, [chr(i) for i in range(ord('A'), ord('Z')+1)]) < 1:
        print("Пароль ненадёжный. Попробуйте ещё раз.")
    else:
        print("Это надёжный пароль!")
        break

