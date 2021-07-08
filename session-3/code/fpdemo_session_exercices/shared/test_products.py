from unittest import TestCase

from shared.products import get_products


class Test(TestCase):
    def test_get_products(self):
        products = get_products();
        print(products)
        self.assertIsNotNone(products)
