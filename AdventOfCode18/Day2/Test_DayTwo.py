import unittest

from Day2 import DayTwo


class TestDayTwo(unittest.TestCase):
    def SetUp(self):
        pass

    def tearDown(self):
        pass

    def test_part1(self):
        data = ['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']
        res = DayTwo.partone(data)
        self.assertEqual(12, res)

    def test_part2(self):
        data = ['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']
        res = DayTwo.parttwo(data)
        self.assertEqual(res, 'fgij')

if __name__ == '__main__':
    unittest.main()
