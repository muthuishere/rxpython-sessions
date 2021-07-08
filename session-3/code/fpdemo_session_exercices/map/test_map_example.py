from unittest import TestCase

from map.map_example import get_ids_from_list_of_users
from shared.users import retrieve_all_users


class Test(TestCase):
    def test_get_user_ids(self):
        results = list(get_ids_from_list_of_users(retrieve_all_users()))
        self.assertIsNotNone(results)
        self.assertEqual(results,[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])

