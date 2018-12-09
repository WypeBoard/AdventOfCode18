import unittest

from Day3 import DayThree as dy


class TestDayThree(unittest.TestCase):
    def SetUp(self):
        pass

    def tearDown(self):
        pass

    def test_part1(self):
        data = ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']
        res = dy.partone(data, 8)
        self.assertEqual(4, res)

    def test_part2(self):
        data = ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']
        res = dy.parttwo(data)
        self.assertEqual(3, res)


if __name__ == '__main__':
    unittest.main()
