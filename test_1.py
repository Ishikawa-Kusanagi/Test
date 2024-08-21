from homeworks_1 import check_age, list_of_numbers, check_month
import unittest


class Homeworks1(unittest.TestCase):

    def test_check_age(self):
        positive = 'Доступ разрешён'
        negative = 'Доступ запрещён'
        for i, (age, expected) in enumerate([
            (14, negative),
            (18, positive),
            (26, positive)
        ]):
            with self.subTest(i):
                result = check_age(age)
                self.assertEqual(expected, result)

    def test_list_of_numbers(self):
        for i, (n, expected) in enumerate([
            (0, []),
            (5, [i for i in range(1, 6)]),
            (10, [i for i in range(1, 11)])
        ]):
            with self.subTest(i):
                result = list_of_numbers(n)
                self.assertEqual(expected, result)

    def test_check_month(self):
        for i, (month, expected) in enumerate([
            (9, 'Осень'),
            (1, 'Зима'),
            (3, 'Весна'),
            (8, 'Лето'),
            (21, 'Некорректный номер месяца')
        ]):
            with self.subTest(i):
                result = check_month(month)
                self.assertEqual(expected, result)
