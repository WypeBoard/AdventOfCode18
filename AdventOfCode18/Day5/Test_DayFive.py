import unittest
from random import shuffle
from Day5 import main as dy


class TestDayFour(unittest.TestCase):
    def SetUp(self):
        pass

    def tearDown(self):
        pass

    def data(self):
        return 'dabAcCaCBAcCcaDA'

    def test_part1(self):
        res = dy.part1(self.data())
        self.assertEqual(10, res)

    def test_part2(self):
        res = dy.part2(self.data())
        self.assertEqual('', res)


if __name__ == '__main__':
    unittest.main()
