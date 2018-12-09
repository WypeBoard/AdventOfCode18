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


def read_csv():
    pass
