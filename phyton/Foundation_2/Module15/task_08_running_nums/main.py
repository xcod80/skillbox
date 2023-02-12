def get_input_parameters():
    """
    Получаем сдвиг и начальны список

    :return: например: [3, [1, 4, -3, 0, 10]]
    :rtype: List[int, List[int]]
    """
    table_list = []
    while True:
        try:
            shift_num = int(input("Сдвиг: "))
            n = int(input("Кол-во элементов списка: "))
        except Exception:
            print("Необходимо ввести целое число!\n")
        else:
            break
    for _ in range(n):
        table_list.append(input("Введите элемент: "))
    return_list = [shift_num, table_list]
    return return_list
    pass


def display_result(shifted_list):
    """
    Выводим получившиеся список

    :param shifted_list: сдвинутый список, например: [5, 1, 2, 3, 4]
    :type shifted_list: List[int]
    """
    print("Сдвинутый список: ", shifted_list)
    pass


def shift_list(shift, original_list):
    """
    Сдвигаем список на определённое количество элементов в право

    :param shift: сдвиг: 3
    :type shift: int
    :param original_list: Исходный список: [1, 4, -3, 0, 10]
    :type original_list: List[int]

    :return: сдвинутый список, например: [5, 1, 2, 3, 4]
    :rtype: List[int]
    """
    if shift >= len(original_list):
        shift -= len(original_list)
    exit_list = original_list[-shift:]
    exit_list.extend(original_list[0:-shift])
    return exit_list
    pass


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    input_data = get_input_parameters()  # получаем параметры
    shift = input_data[0]
    original_list = input_data[1]
    shifted_list = shift_list(shift, original_list)  # сдвигаем список.
    display_result(shifted_list)  # выводим результат
