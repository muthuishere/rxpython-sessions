from unittest import TestCase

from reactive.chapter4_test_observable.simple_observable import products_with_just, products_with_from_
from rx import operators as ops

class Test(TestCase):
    def test_products_with_just(self):
        result = products_with_just().run()
        self.assertTrue(isinstance(result, list))

    def test_products_with_from_with_run(self):
        result = products_with_from_().run()
        print(type(result))
        print(result)
        self.assertTrue(isinstance(result, dict))

    def test_products_with_from_with_run_and_iterable(self):
        result = products_with_from_().pipe(ops.to_iterable()).run()
        print(type(result))
        self.assertTrue(isinstance(result, list))

