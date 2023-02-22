alphabet = [chr(s) for s in range(ord("а"),ord("я")+1)]
input_text = input("Введите сообщение: ").lower()
shift = int(input("Введите свдвиг: "))
print("Зашифрованное сообщение:", end = ' ')
for symbol in input_text:
    if symbol.isspace():
        print(symbol, end = '')
    else:
        print(alphabet[(alphabet.index(symbol) + shift)%len(alphabet)], end = '')
print()