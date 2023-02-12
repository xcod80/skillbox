import unittest

from task_06_word_analysis.main import count_number_unique_letters


class Test06CountNumberUniqueLetters(unittest.TestCase):
    def test_main_privet(self):
        """
        Проверяем обычный кейс. При вводе "привет"  должны получить "Кол-во уникальных букв: 6"
        """
        number_unique_letters = count_number_unique_letters("привет")

        self.assertEqual(6, number_unique_letters)

    def test_main_lava(self):
        """
        Проверяем обычный кейс. При вводе "лава"  должны получить "Кол-во уникальных букв: 2"
        """
        number_unique_letters = count_number_unique_letters("лава")

        self.assertEqual(2, number_unique_letters)


if __name__ == '__main__':
    unittest.main()
