def get_input_parameters():
    """
    Получаем список фильмов, которые пользователь хочет добавить в "любимые"

    :return: добавляемые фильмы, например: ["Леон", "Безумный Макс", "Мементо", "Царь горы"]
    :rtype: List[str]
    """
    film_list = []
    while True:
        try:
            n = int(input("Сколько фильмов хотите добавить? "))
        except Exception:
            print("Необходимо ввести целое число!\n")
        else:
            break
    for i in range(n):
        film_list.append(input(f'Введите название фильма:'))
    return film_list
    pass


def display_result(favorite_films, errors):
    """
    Выводим список ошибок и список любимых фильмов

    :param favorite_films: список любимых фильмов, например: ["Леон", "Мементо"]
    :type favorite_films: List[str]
    :param errors: список ненайденных фильмов, например: ["Безумный Макс", "Царь горы"]
    :type errors: List[str]
    """
    for film in errors:
        print(f'Ошибка: фильма {film} у нас нет :(')
    print("Ваш список любимых фильмов:", end='')
    for film in favorite_films:
        print(film,", ", end='')
    print("\b\b")
    pass


def add_favorite_film(new_favorite_films, available_films):
    """
    Добавляем фильмы в список "любимых".

    :param new_favorite_films: фильмы, которые нужно добавить в "любимые",
           например: ["Леон", "Безумный Макс", "Мементо", "Царь горы"]
    :type new_favorite_films: List[str]
    :param available_films: фильмы, которые есть на киносайте,
           например: ["Леон", "Назад в будущее", "Мементо"]
    :type available_films: List[str]

    :return: Список фильмов в списке "любимых" и список не найденных фильмов,
             например: (["Леон", "Мементо"], ["Безумный Макс", "Царь горы"])
    :rtype: Tuple[List[str], List[str]]
    """
    err_list, fav_films = [], []
    for film in new_favorite_films:
        if film in available_films:
            fav_films.append(film)
        else:
            err_list.append(film)
    return fav_films, err_list
    pass


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    available_films = [
        "Крепкий орешек", "Назад в будущее", "Таксист",
        "Леон", "Богемская рапсодия", "Город грехов",
        "Мементо", "Отступники", "Деревня"
    ]
    new_favorite_films = get_input_parameters()  # получаем параметры
    favorite_films, errors = add_favorite_film(
        new_favorite_films,
        available_films
    )  # добавлем фильмы в список "любимых".
    display_result(favorite_films, errors)  # выводим результат
