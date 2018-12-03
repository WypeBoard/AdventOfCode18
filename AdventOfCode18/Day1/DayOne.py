def partone(data):
    return sum(data)


def parttwo(data):
    previous_sum = [0]
    i = 0
    while True:
        calc = data[i % len(data)] + previous_sum[i]
        if calc in previous_sum:
            print(i)
            return calc
        else:
            i = i + 1
            previous_sum.append(calc)


def read_file(file_path):
    """
    Read from a file called systemparamter.csv
    The file has to be defined as:
    x;y;z
    x1;y1;z1

    Note:
        semicolon (;) seperation
        newline (\n) defines new entry
    """
    with open(file_path, 'r', newline='') as file:
        return [x.strip() for x in list(file.readlines())]


if __name__ == '__main__':
    values = read_file('inputDayOne.csv')
    data = []
    for value in values:
        data.append(int(value))
    print(partone(data))
    print(parttwo(data))
