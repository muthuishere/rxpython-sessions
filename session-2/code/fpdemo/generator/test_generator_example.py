from unittest import TestCase

from generator.generator_example import multiples_of_248_till, multiples_of_248_till_v0
import cProfile
import pstats

class Test(TestCase):
    def test_multiples_of_248_till(self):
        profiler = cProfile.Profile()
        profiler.enable()

        result = multiples_of_248_till(5600000)

        profiler.disable()
        pstats.Stats(profiler).print_stats()


        first_value = next(result)
        print(first_value)
        self.assertEqual(first_value,248)
        self.assertIsNotNone(result)
