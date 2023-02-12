def get_input_parameters():
    """
    Получаем набор клеток

    :return: набор клеток, например: [3, 0, 6, 2, 10]
    :rtype: List[int]
    """
    cells_list = []
    while True:
        try:
            N = int(input("Кол-во клеток: "))
        except Exception:
            print("Необходимо ввести целое число!\n")
        else:
            break
    for i in range(N):
        while True:
            try:
                cells_list.append(int(input(f'Эффективность {i+1} клетки:')))
            except Exception:
                print("Необходимо ввести целое число!\n")
            else:
                break
    return cells_list
    pass


def display_result(cells):
    """
    Выводим список клеток у которых значение меньше индекса

    :param cells: набор клеток, например: [0, 2]
    :type cells: List[int]
    """
    print("Неподходящие значения:", end='')
    for i in range(len(cells)):
        print(cells[i]," ", end='')
    print()
    pass


def select_cells(cells):
    """
    Отбираем список клеток, у которых значение меньше индекса.

    :param cells: набор клеток, например: [3, 0, 6, 2, 10]
    :type cells: List[int]

    :return: набор подходящих клеток, например: [0, 2]
    :rtype: List[int]
    """
    return [cells[i] for i in range(len(cells)) if i+1 > cells[i]]
    pass


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    cells = get_input_parameters()  # получаем параметры
    result_cells = select_cells(cells)  # отбираем клетки
    display_result(result_cells)  # выводим результат
