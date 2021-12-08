from unittest import TestCase
from ..solution import Digit

class Test(TestCase):

    def test_sum(self):
        self.assertEquals(Digit('a').digit, None)
        self.assertEquals(Digit('ab').digit, 1)
        self.assertEquals(Digit('abc').digit, 7)
        self.assertEquals(Digit('abcd').digit, 4)
        self.assertEquals(Digit('abcde').digit, None)
        self.assertEquals(Digit('abcdef').digit, None)
        self.assertEquals(Digit('abcdefg').digit, 8)