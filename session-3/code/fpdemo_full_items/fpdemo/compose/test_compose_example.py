from unittest import TestCase

from compose.compose_example import total_salaries_for_gender
from shared.users import get_users


class Test(TestCase):
    def test_total_salaries_for_gender(self):
        result = total_salaries_for_gender(get_users(),'Female')
        print(result)
        self.assertGreater(result,100)
        self.assertEqual(result,738875)
