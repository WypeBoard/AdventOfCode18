def partone(data):
    two = 0
    three = 0
    for string in data:
        checked = []
        checkTwo = False
        checkThree = False
        for char in string:
            if char in checked:
                continue
            i = string.count(char)
            if i == 2 and not checkTwo:
                checked.append(char)
                checkTwo = True
                two = two + 1
            elif i == 3 and not checkThree:
                checked.append(char)
                checkThree = True
                three = three + 1
    return two * three


def parttwo(data):
    for string in data:
        for check in data:
            res = []
            if string == check:
                continue
            mismatch = 0
            for i in range(len(string)):
                if string[i] != check[i]:
                    mismatch = mismatch + 1
                else:
                    res.append(string[i])
                if mismatch > 1:
                    break
            if mismatch == 1:
                return ''.join(res)



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
    values = read_file('input.csv')
    print(partone(values))
    print(parttwo(values))
