class Grid:

    def __init__(self, row):
        self.id = None
        self.startTop = 0
        self.startLeft = 0
        self.width = 0
        self.height = 0
        self.parse(row)

    def __str__(self):
        return 'id: ' + str(self.id) + '\n'\
               'startTop: ' + str(self.startTop) + '\n'\
               'startLeft: ' + str(self.startLeft) + '\n'\
               'width: ' + str(self.width) + '\n'\
               'heigh: ' + str(self.height)

    def parse(self, row):
        part = row.split()
        self.id = part[0]
        position = part[2].split(',')
        self.startTop = int(position[1][:-1])
        self.startLeft = int(position[0])
        size = part[3].split('x')
        self.width = int(size[0])
        self.height = int(size[1])
        pass

    def get_id(self):
        return self.id

    def get_start_position(self):
        return self.startTop, self.startLeft

    def get_size(self):
        return self.height, self.width

