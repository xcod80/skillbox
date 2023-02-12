import unittest

from task_05_movie.main import add_favorite_film


class Test05AddFavoriteFilm(unittest.TestCase):
    def test_add_favorite_film(self):
        """
        Проверяем обычный кейс. При вводе ["Леон", "Безумный Макс", "Мементо", "Царь горы"]
         должны получить (["Леон", "Мементо"], ["Безумный Макс", "Царь горы"])
        """
        available_films = [
            "Крепкий орешек", "Назад в будущее", "Таксист",
            "Леон", "Богемская рапсодия", "Город грехов",
            "Мементо", "Отступники", "Деревня"
        ]
        new_favorite_films = ["Леон", "Безумный Макс", "Мементо", "Царь горы"]

        favorite_films, errors = add_favorite_film(new_favorite_films,available_films )

        self.assertEqual({"Леон", "Мементо"}, set(favorite_films))
        self.assertEqual({"Безумный Макс", "Царь горы"}, set(errors))


if __name__ == '__main__':
    unittest.main()
