
class Grid:
    def __init__(self, w, h, init_with=None):
        self.items = []
        self.width = w
        self.height = h
        for _ in range(w * h):
            self.items.append(init_with)

    def _index_from_coords(self, x, y):
        return x + self.width * y

    def set(self, x, y, obj):
        self.items[self._index_from_coords(x, y)] = obj

    def get(self, x, y):
        return self.items[self._index_from_coords(x, y)]

    def __str__(self):
        ret_str = ""
        for y in reversed(range(self.height)):
            for x in range(self.width):
                ret_str += self.items[self._index_from_coords(x, y)]
            ret_str += "\n"
        return ret_str
