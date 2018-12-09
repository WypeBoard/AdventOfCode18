from Day3.Grid import Grid
from collections import defaultdict
import re


def result(data, part):
    grid = map(lambda s: map(int, re.findall(r'-?\d+', s)), data)
    matrix = defaultdict(list)
    overlaps = {}
    for (id, x, y, width, height) in grid:
        overlaps[id] = set()
        for i in range(x, x + width):
            for j in range(y, y + height):
                if matrix[(i, j)]:
                    for number in matrix[(i, j)]:
                        overlaps[id].add(number)
                        overlaps[number].add(id)
                matrix[(i, j)].append(id)
    if part == 1:
        return len([k for k in matrix if len(matrix[k]) > 1])
    return [k for k in overlaps if len(overlaps[k]) == 0][0]


def createGrid(matrix, grid):
    return matrix


def partone(data, length):
    matrix = [[0 for i in range(length)] for j in range(length)]
    res = 0
    for row in data:
        grid = Grid(row)
        top, left = grid.get_start_position()
        bottom, right = grid.get_size()
        for i in range(bottom):
            for j in range(right):
                try:
                    matrix[top + i][left + j] = matrix[top + i][left + j] + 1
                except IndexError:
                    print(str(grid) + " failed")
                    raise
    for i in range(length):
        for j in range(length):
            if matrix[i][j] > 1:
                res = res + 1
    return res


def parttwo(data, length):
    matrix = [[0 for i in range(length)] for j in range(length)]
    partres = set()
    for row in data:
        grid = Grid(row)
        skip = False
        top, left = grid.get_start_position()
        bottom, right = grid.get_size()
        for i in range(bottom):
            for j in range(right):
                res = matrix[top + i][left + j] + 1
                matrix[top + i][left + j] = res
                if res > 1:
                    skip = True
        if skip:
            continue
        partres.add(grid.get_id())
    grids = []
    for row in data:
        grids.append(Grid(row))
    for i in partres:
        grids[i]
    pass


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
    print(result(values, 1))
    print(result(values, 2))
    print(partone(values, 1000))
    print(parttwo(values))
