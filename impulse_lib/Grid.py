class Grid:
    def __init__(self, default=None):
        self.items = {}
        self.default = default
        self.width = 0
        self.height = 0

    def set(self, x, y, obj):
        self.items[(x, y)] = obj
        self.width = max([x + 1, self.width])
        self.height = max([y + 1, self.height])

    def get(self, x, y):
        self.items.get((x, y), self.default)

    def pop(self, x, y):
        ret_obj = self.items.pop((x, y), self.default)

        # Recalculate width/height
        if not ret_obj == self.default:
            x_coords = [coord[0] for coord in self.items.keys()]
            y_coords = [coord[1] for coord in self.items.keys()]
            x_coords.append(-1)
            y_coords.append(-1)
            self.width = max(x_coords) + 1
            self.height = max(y_coords) + 1

        return ret_obj

    def __str__(self):
        ret_str = ""
        if self.width > 0 and self.height > 0:
            for y in reversed(range(self.height)):
                for x in range(self.width):
                    ret_str += str(self.items.get((x, y), self.default))

                ret_str += "\n"
        else:
            ret_str = ""
        return ret_str


def _test_Grid():
    results = []

    size_tests = [
        {'default': "_", 'coords': [], 'objects': [], 'exp_str': ""},
        {'default': "_", 'coords': [(1, 1)], 'objects': ["X"], 'exp_str': "_X\n__\n"},
        {'default': "_", 'coords': [(2, 1)], 'objects': ["X"],
         'exp_str':
             "__X\n"
             "___\n"},
        {'default': "_", 'coords': [(1, 2)], 'objects': ["X"],
         'exp_str':
             "_X\n"
             "__\n"
             "__\n"},
        {'default': "_", 'coords': [(2, 2)], 'objects': ["X"],
         'exp_str':
             "__X\n"
             "___\n"
             "___\n"},
        {'default': "_", 'coords': [(5, 5)], 'objects': ["X"],
         'exp_str':
             "_____X\n"
             "______\n"
             "______\n"
             "______\n"
             "______\n"
             "______\n"},
    ]

    for test_num, size_test in enumerate(size_tests):
        g = Grid(size_test['default'])
        for index, coord in enumerate(size_test['coords']):
            g.set(coord[0], coord[1], size_test['objects'][index])
        actual_str = g.__str__()
        if actual_str == size_test['exp_str']:
            results.append("SIZE TEST {}: PASS".format(test_num))
        else:
            results.append("SIZE TEST {}: FAIL".format(test_num))

    io_tests = [
        {'default': "_", 'coords': [(1, 1), (0, 1)], 'objects': ["X", "Y"], 'full_str': "YX\n__\n",
         'pop_coords': [(1, 1), (0, 1)], 'exp_val': ["X", "Y"], 'exp_str': ["Y\n_\n", ""]},
        {'default': "_", 'coords': [(20, 1), (5, 0)], 'objects': ["X", "Y"],
         'full_str':
             "____________________X\n"
             "_____Y_______________\n",
         'pop_coords': [(20, 1), (5, 0)], 'exp_val': ["X", "Y"], 'exp_str': ["_____Y\n", ""]},
    ]

    for test_num, io_test in enumerate(io_tests):
        g = Grid(io_test['default'])
        for index, coord in enumerate(io_test['coords']):
            g.set(coord[0], coord[1], io_test['objects'][index])
        actual_str = g.__str__()
        results.append("IO TEST {}, all coords added: {}"
                       .format(test_num,
                               "PASS" if actual_str == io_test['full_str'] else "FAIL"))

        for coord_num, coords in enumerate(io_test['pop_coords']):
            actual_obj = g.pop(coords[0], coords[1])
            results.append("IO TEST {}, pop item {}: {}"
                           .format(test_num, coord_num,
                                   "PASS" if actual_obj == io_test['exp_val'][coord_num] else "FAIL"))
            grid_after = g.__str__()
            results.append("IO TEST {}, grid after {}: {}"
                           .format(test_num, coord_num,
                                   "PASS" if grid_after == io_test['exp_str'][coord_num] else "FAIL"))

    # Print results
    for result in results:
        print result
