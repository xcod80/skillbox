def get_input_parameters():
    """
    Получаем входное слово

    :return: входное слово, например: "привет"
    :rtype: str
    """
    return input("Введите слово:")
    pass


def display_result(number_unique_letters):
    """
    Выводим количество уникальных букв в слове

    :param number_unique_letters: количество уникальных букв в слове, например: 6
    :type number_unique_letters: int
    """
    print("Количество уникальных букв:", number_unique_letters)
    pass


def count_number_unique_letters(word):
    """
    Считаем количество уникальных букв в слове.

    :param word: входное слово, например: "привет"
    :type word: str

    :return: количество уникальных букв в слове, например: 6
    :rtype: int
    """
    uniq_symbol = 0
    for symbol in word:
        if word.count(symbol) == 1:
            uniq_symbol +=1
    return uniq_symbol
    pass


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    word = get_input_parameters()  # получаем параметры
    number_unique_letters = count_number_unique_letters(word)  # считаем количество уникальных букв.
    display_result(number_unique_letters)  # выводим результат
