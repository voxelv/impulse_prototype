class ContinuousGrid:
    def __init__(self, default=None):
        self.items = {}
        self.default = default
        self.width = 0
        self.height = 0
        self.low_left_coord = (0, 0)

    def _filter_coords(self, x, y):
        if not isinstance(x, int):
            raise TypeError("x coord is not an integer!")
        if not isinstance(y, int):
            raise TypeError("y coord is not an integer!")
        return x, y

    def _recalc_w_h(self):
        def _one_pass_min_max(iterable):
            min_val = iterable[0]
            max_val = iterable[0]
            for item in iterable:
                min_val = min(item, min_val)
                max_val = max(item, max_val)
            return min_val, max_val

        self.width = 0
        self.height = 0
        xcoords = [coord[0] for coord in self.items.keys()]
        ycoords = [coord[1] for coord in self.items.keys()]
        if len(xcoords) > 0 and len(ycoords) > 0:
            minx, maxx = _one_pass_min_max(xcoords)
            self.width = maxx - minx + 1
            miny, maxy = _one_pass_min_max(ycoords)
            self.height = maxy - miny + 1
            self.low_left_coord = (minx, miny)

    def set(self, x, y, obj):
        x, y = self._filter_coords(x, y)
        self.items[(x, y)] = obj
        self._recalc_w_h()

    def get(self, x, y):
        x, y = self._filter_coords(x, y)
        self.items.get((x, y), self.default)

    def pop(self, x, y):
        x, y = self._filter_coords(x, y)
        ret_obj = self.items.pop((x, y), self.default)

        self._recalc_w_h()

        return ret_obj

    def __str__(self):
        ret_str = ""
        if len(self.items.keys()) == 0:
            ret_str = ""
        elif len(self.items.keys()) == 1:
            ret_str = "{}\n".format(str(self.items.values()[0]))
        else:
            for y in reversed(range(self.height)):
                y += self.low_left_coord[1]
                for x in range(self.width):
                    x += self.low_left_coord[0]
                    ret_str += str(self.items.get((x, y), self.default))
                ret_str += "\n"

        return ret_str


def _test_ContinuousGrid():
    results = []

    size_tests = [
        {'default': "_", 'coords': [], 'objects': [], 'exp_str': ""},
        {'default': "_", 'coords': [(0, 0)], 'objects': ["X"], 'exp_str': "X\n"},
        {'default': "_", 'coords': [(1, 1)], 'objects': ["X"], 'exp_str': "X\n"},
        {'default': "_", 'coords': [(-1, -1)], 'objects': ["X"], 'exp_str': "X\n"},
        {'default': "_", 'coords': [(7, 7)], 'objects': ["X"], 'exp_str': "X\n"},
    ]

    for test_num, size_test in enumerate(size_tests):
        g = ContinuousGrid(size_test['default'])
        for index, coord in enumerate(size_test['coords']):
            g.set(coord[0], coord[1], size_test['objects'][index])
        actual_str = g.__str__()
        print actual_str
        if actual_str == size_test['exp_str']:
            results.append("SIZE TEST {}: PASS".format(test_num))
        else:
            results.append("SIZE TEST {}: FAIL".format(test_num))

    io_tests = [
        {'default': "_", 'coords': [(1, 1), (0, 1)], 'objects': ["X", "Y"], 'full_str': "YX\n",
         'pop_coords': [(1, 1), (0, 1)], 'exp_val': ["X", "Y"], 'exp_str': ["Y\n", ""]},
        {'default': "_", 'coords': [(20, 1), (5, 0)], 'objects': ["X", "Y"],
         'full_str':
             "_______________X\n"
             "Y_______________\n",
         'pop_coords': [(20, 1), (5, 0)], 'exp_val': ["X", "Y"], 'exp_str': ["Y\n", ""]},
    ]

    for test_num, io_test in enumerate(io_tests):
        g = ContinuousGrid(io_test['default'])
        for index, coord in enumerate(io_test['coords']):
            g.set(coord[0], coord[1], io_test['objects'][index])
        actual_str = g.__str__()
        print actual_str
        results.append("IO TEST {}, all coords added: {}"
                       .format(test_num,
                               "PASS" if actual_str == io_test['full_str'] else "FAIL"))

        for coord_num, coords in enumerate(io_test['pop_coords']):
            actual_obj = g.pop(coords[0], coords[1])
            results.append("IO TEST {}, pop item {}: {}"
                           .format(test_num, coord_num,
                                   "PASS" if actual_obj == io_test['exp_val'][coord_num] else "FAIL"))
            grid_after = g.__str__()
            print grid_after
            results.append("IO TEST {}, grid after {}: {}"
                           .format(test_num, coord_num,
                                   "PASS" if grid_after == io_test['exp_str'][coord_num] else "FAIL"))

    # Print results
    for result in results:
        print result
