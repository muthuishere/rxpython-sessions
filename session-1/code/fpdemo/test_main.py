from unittest import TestCase

from main import canDrive


class Test(TestCase):
    def test_can_drive(self):
        self.assertFalse(canDrive(12))
