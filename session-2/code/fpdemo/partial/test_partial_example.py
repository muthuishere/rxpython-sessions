from unittest import TestCase

from partial.partial_example import add_two_numbers_and_multiply_third, add_two_numbers, multiply_two_numbers, \
    increment_one


class Test(TestCase):
    def test_add_two_numbers_and_multiply_third(self):
        self.assertEqual(add_two_numbers_and_multiply_third(1, 2, 3), 9)

    def test_add_two_numbers(self):
        self.assertEqual(add_two_numbers(1, 2), 3)

    def test_multiply_two_numbers(self):
        self.assertEqual(multiply_two_numbers(y = 1, z = 2), 2)

    def test_increment_one(self):
        self.assertEqual(increment_one(23), 24)

