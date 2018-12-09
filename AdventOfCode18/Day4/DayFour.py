import Readfile as rf
from dateutil import parser
from collections import defaultdict

def caldulate(data):
    guards = defaultdict(list)
    times = defaultdict(int)

    for k in sorted(data):
        time, action = k.split('] ')
        time = parser.parse(time[1:])

        if action.startswith('Guard'):
            guard = int(action.split()[1][1:])
        elif action == 'falls asleep':
            start = time
        elif action == 'wakes up':
            end = time
            guards[guard].append((start.minute, end.minute))
            times[guard] += (end-start).seconds
    return guards, times


def part1(data):
    guards, times = caldulate(data)
    (guard, time) = max(times.items(), key=lambda i: i[1])
    (minute, count) = max([(minute, sum(1 for start, end in guards[guard] if start <= minute < end)) for minute in range(60)], key=lambda i: i[1])
    return minute * guard


def part2(data):
    guards, times = caldulate(data)
    (guard, minute, count) = max([
        (guard, minute, sum(1 for start, end in guards[guard] if start <= minute < end))
        for minute in range(60) for guard in guards], key=lambda i: i[0])
    return guard * minute


if __name__ == '__main__':
    data = rf.read_file('InputFour')
    print(part1(data))
    print(part2(data))
