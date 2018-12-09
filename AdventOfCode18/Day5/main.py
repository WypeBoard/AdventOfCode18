import Readfile as rf


def part1(line):
    oldline = ''
    while oldline != line:
        oldline = line
        for i in range(26):
            line = line.replace(chr(ord('a') + i) + chr(ord('A') + i), '')
            line = line.replace(chr(ord('A') + i) + chr(ord('a') + i), '')
    return len(line)


def part2(line):
    res = len(line)
    for i in range(26):
        templine = line
        templine = templine.replace(chr(ord('a') + i), '')
        templine = templine.replace(chr(ord('A') + i), '')
        templine = part1(templine)
        res = templine if templine < res else res
    return res


if __name__ == '__main__':
    data = rf.read_file('input')
    print(part1(data[0]))
    print(part2(data[0]))
