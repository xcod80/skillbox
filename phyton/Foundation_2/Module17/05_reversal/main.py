symbols = input("Введите строку: ")
while symbols.count('h') < 2:
    symbols = input("Введите строку: ")
print("Развёрнутая последовательность между первым и последним h:", symbols[symbols.index("h")+1:symbols.rindex("h")][::-1])