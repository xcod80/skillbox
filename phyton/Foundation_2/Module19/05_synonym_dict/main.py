word_dict = dict()
for i in range(int(input('Введите количество пар слов: '))):
    mini_dict = input('Введите пару слов:').lower().split('-')
    word_dict[mini_dict[0].strip()] = mini_dict[1].strip()
    word_dict[mini_dict[1].strip()] = mini_dict[0].strip()
print('\n')
while True:
    key_word = input('Введите слово: ')
    if word_dict.get(key_word) != None:
        print('Синоним:', word_dict[key_word].capitalize())
        break
    else:
        print('Такого слова в словаре нет.')