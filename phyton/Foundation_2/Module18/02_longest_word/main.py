words_list = input('Введите строку: ').split()
print("Самое длинное слово:", max(words_list, key=len))
print("Длина этого слова:", len(max(words_list, key=len)))
