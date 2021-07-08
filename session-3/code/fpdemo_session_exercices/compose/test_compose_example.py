from unittest import TestCase

from compose.compose_example import total_salaries_for_gender
from shared.users import retrieve_all_users


class Test(TestCase):
    def test_total_salaries_for_gender(self):
        result = total_salaries_for_gender(retrieve_all_users(), 'Female')
        print(result)
        self.assertGreater(result,100)
        self.assertEqual(result,738875)
