def get_input_parameters():
    """
    Получаем список видеокарт

    :return: набор видеокарт, например: [3070, 2060, 3090, 3070, 3090]
    :rtype: List[int]
    """
    cards_list = []
    while True:
        try:
            n = int(input("Кол-во видеокарт: "))
        except Exception:
            print("Необходимо ввести целое число!\n")
        else:
            break
    for i in range(n):
        while True:
            try:
                cards_list.append(int(input(f'Видеокарта №{i+1}:')))
            except Exception:
                print("Необходимо ввести целое число!\n")
            else:
                break
    return cards_list
    pass


def display_result(old_video_cards, new_video_cards):
    """
    Выводим список оставшихся видеокарт

    :param old_video_cards: старый набор видеокарт, например: [3070, 2060, 3090, 3070, 3090]
    :type old_video_cards: List[int]
    :param new_video_cards: новый набор видеокарт, например: [3070, 2060, 3070]
    :type new_video_cards: List[int]
    """
    print("Старый список видеокарт:", old_video_cards)
    print("Новый список видеокарт:", new_video_cards)

    pass


def select_video_cards(video_cards):
    """
    Удаляем из списка видеокарт наибольшие элементы.

    :param video_cards: набор видеокарт, например: [3070, 2060, 3090, 3070, 3090]
    :type video_cards: List[int]

    :return: набор оставшихся видеокарт, например: [3070, 2060, 3070]
    :rtype: List[int]
    """
    key_value = max(video_cards)
    # while key_value in video_cards:
    #     video_cards.remove(key_value)
    # return video_cards
    new_card_list = []
    for card in video_cards:
        if card != key_value:
            new_card_list.append(card)
    return new_card_list
    pass


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    video_cards = get_input_parameters()  # получаем параметры
    result_video_cards = select_video_cards(video_cards)  # удаляет наибольшие элементы.
    display_result(video_cards, result_video_cards)  # выводим результат
