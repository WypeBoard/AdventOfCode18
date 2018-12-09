import unittest
from random import shuffle
from Day4 import DayFour as dy


class TestDayFour(unittest.TestCase):
    def SetUp(self):
        pass

    def tearDown(self):
        pass

    def data(self):
        _data = []
        _data.append('[1518-11-01 00:00] Guard  #10 begins shift')
        _data.append('[1518-11-01 00:05] falls asleep')
        _data.append('[1518-11-01 00:25] wakes up')
        _data.append('[1518-11-01 00:30] falls asleep')
        _data.append('[1518-11-01 00:55] wakes up')
        _data.append('[1518-11-01 23:58] Guard  #99 begins shift')
        _data.append('[1518-11-02 00:40] falls asleep')
        _data.append('[1518-11-02 00:50] wakes up')
        _data.append('[1518-11-03 00:05] Guard  #10 begins shift')
        _data.append('[1518-11-03 00:24] falls asleep')
        _data.append('[1518-11-03 00:29] wakes up')
        _data.append('[1518-11-04 00:02] Guard  #99 begins shift')
        _data.append('[1518-11-04 00:36] falls asleep')
        _data.append('[1518-11-04 00:46] wakes up')
        _data.append('[1518-11-05 00:03] Guard  #99 begins shift')
        _data.append('[1518-11-05 00:45] falls asleep')
        _data.append('[1518-11-05 00:55] wakes up')
        shuffle(_data)
        return _data

    def test_part1(self):
        res = dy.part1(self.data())
        self.assertEqual(240, res)

    def test_part2(self):
        res = dy.part2(self.data())
        self.assertEqual(4455, res)


if __name__ == '__main__':
    unittest.main()
