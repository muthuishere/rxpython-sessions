from unittest import TestCase

from filter.filter_example import get_users_of_gender
from shared.users import get_users


class Test(TestCase):
    def test_get_users_of_gender(self):
        results = list(get_users_of_gender(get_users(),'Female'))
        print(results)
        totalusers = len(results)
        print("totalusers",totalusers)
        self.assertGreater(totalusers,1)
        self.assertEqual(totalusers,7)
