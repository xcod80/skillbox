vowel_list = "аеёиоуыэюя"
text_string = input("Введите текст: ")

symbol_list = [symbol for symbol in text_string if symbol in vowel_list]
print("Список гласных букв:", symbol_list)
print("Длина списка:", len(symbol_list))
