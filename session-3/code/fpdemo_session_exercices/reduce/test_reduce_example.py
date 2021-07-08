from unittest import TestCase

from reduce.reduce_example import total_salaries_for
from shared.users import retrieve_all_users


class Test(TestCase):
    def test_total_salaries_for(self):
        total_salaries = total_salaries_for(retrieve_all_users())
        print(total_salaries)
        self.assertGreater(total_salaries, 1000)
        self.assertEqual(total_salaries, 2206427)
