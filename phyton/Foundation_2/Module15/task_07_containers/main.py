def get_input_parameters():
    """
    Получаем список весов контейнеров и вес нового контейнера
    Незабываем проверит данные: все числа целые и не превышают 200.

    :return: список весов контейнеров и вес нового контейнера,
             например: [[165, 163, 160, 160, 157, 157, 155, 154], 162]
    :rtype: List[List[int], int]
    """
    cargo_list = []
    while True:
        try:
            n = int(input("Кол-во контейнеров: "))
        except Exception:
            print("Необходимо ввести целое число!\n")
        else:
            break
    for i in range(n):
        while True:
            try:
                cargo_list.append(int(input("Введите вес контейнера: ")))
            except Exception:
                print("Необходимо ввести целое число!\n")
            else:
                if cargo_list[i] > 200:
                    print("Вес не может превышать 200!!!")
                    del cargo_list[i]
                else:
                    break
    while True:
        try:
            new_cargo = int(input("Введите вес нового контейнера: "))
        except Exception:
            print("Необходимо ввести целое число!\n")
        else:
            if new_cargo > 200:
                print("Вес не может превышать 200!!!")
            else:
                break
    return_list = [cargo_list, new_cargo]
    return return_list
    pass


def display_result(serial_number_new_container):
    """
    Выводим порядковый номер нового контейнера.

    :param serial_number_new_container: порядковый номер нового контейнера, например: 3
    :type serial_number_new_container: int
    """
    print("Номер, куда встанет новый контейнер:", serial_number_new_container)
    pass


def search_serial_number_new_container(list_container_weights, new_container_weight):
    """
    Ищем куда вставим новый контейнер.

    :param list_container_weights: список весов контейнеров, например: [165, 163, 160, 160, 157, 157, 155, 154]
    :type list_container_weights: List[int]
    :param new_container_weight: вес нового контейнера, например: 166
    :type new_container_weight: int

    :return: порядковый номер нового контейнера, например: 3
    :rtype: int
    """
    list_container_weights.sort(reverse=True)
    for weight in list_container_weights:
        if weight < new_container_weight:
            return list_container_weights.index(weight)+1
    else:
        return len(list_container_weights)+1
    pass


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    input_data = get_input_parameters()  # получаем параметры
    list_container_weights = input_data[0]
    new_container_weight = input_data[1]
    # Ищем куда вставим новый контейнер.
    serial_number_new_container = search_serial_number_new_container(list_container_weights, new_container_weight)
    display_result(serial_number_new_container)  # выводим результат
