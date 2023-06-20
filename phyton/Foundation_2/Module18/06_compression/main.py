input_string = input("Введите строку: ")
RLE_string = ''
sym_number = 1
for i in range(1, len(input_string)):
    if not input_string[i] == input_string[i-1]:
        RLE_string += input_string[i-1] + str(sym_number)
        sym_number = 1
    else:
        sym_number += 1
else:
    RLE_string += input_string[i] + str(sym_number)
print("Закодированная строка:", RLE_string)