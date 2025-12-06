from unittest import TestCase

from day_one_part_two import get_password


class Test(TestCase):
    def test_get_password(self):
        assert get_password("test.txt") == 6
