import unittest

from Day1 import DayOne


class TestDayOne(unittest.TestCase):
    def SetUp(self):
        pass

    def tearDown(self):
        pass

    def test_part_one1(self):
        data_input = [1, 1, 1]
        res = DayOne.partone(data_input)

        self.assertEqual(res, 3)

    def test_part_one2(self):
        data_input = [1, 1, -2]
        res = DayOne.partone(data_input)

        self.assertEqual(res, 0)

    def test_part_one3(self):
        data_input = [-1, -2, -3]
        res = DayOne.partone(data_input)

        self.assertEqual(res, -6)

    def test_part_two1(self):
        data_input = [1, -2, 3, 1]
        res = DayOne.parttwo(data_input)

        self.assertEqual(res, 2)

    def test_part_two2(self):
        data_input = [1, -1]
        res = DayOne.parttwo(data_input)

        self.assertEqual(res, 0)

    def test_part_two3(self):
        data_input = [3, 3, 4, -2, -4]
        res = DayOne.parttwo(data_input)

        self.assertEqual(res, 10)

    def test_part_two4(self):
        data_input = [-6, 3, 8, 5, -6]
        res = DayOne.parttwo(data_input)

        self.assertEqual(res, 5)

    def test_part_two5(self):
        data_input = [7, 7, -2, -7, -4]
        res = DayOne.parttwo(data_input)

        self.assertEqual(res, 14)

if __name__ == '__main__':
    unittest.main()