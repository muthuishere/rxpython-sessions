
from unittest import TestCase
from lambda_example import a_plus_b_whole_square, a_minus_b_whole_square


class Test(TestCase):
    def test_a_plus_b_whole_square(self):
        self.assertEqual(a_plus_b_whole_square(1 ,2) ,9)
    def test_a_minus_b_whole_square(self):
        self.assertEqual(a_minus_b_whole_square(1 ,2) ,1)

