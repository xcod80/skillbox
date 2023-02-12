def get_input_parameters():
    """
    Получаем неотсортированный список чисел

    :return: неотсортированный список чисел, например: [1, 4, -3, 0, 10]
    :rtype: List[int]
    """
    nums_list = []
    while True:
        try:
            n = int(input("Количество чисел: "))
        except Exception:
            print("Необходимо ввести целое число!\n")
        else:
            break
    for i in range(n):
        while True:
            try:
                nums_list.append(int(input(f'Число №{i+1}:')))
            except Exception:
                print("Необходимо ввести целое число!\n")
            else:
                break
    print("Изначальный список: ", nums_list,"\n")
    return nums_list
    pass


def display_result(sorted_list):
    """
    Выводим отсортированный список

    :param sorted_list: отсортированный список, например: [-3, 0, 1, 4, 10]
    :type sorted_list: List[int]
    """
    print("Отсортированный список:", sorted_list)
    pass


def sort_list(original_list):
    """
    Сортируем список

    :param original_list: Исходный список: [1, 4, -3, 0, 10]
    :type original_list: List[int]

    :return: отсортированный, например: [-3, 0, 1, 4, 10]
    :rtype: List[int]
    """
    original_list.sort()
    return original_list
    pass


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    original_list = get_input_parameters()  # получаем параметры
    sorted_list = sort_list(original_list)  # сортируем список.
    display_result(sorted_list)  # выводим результат
