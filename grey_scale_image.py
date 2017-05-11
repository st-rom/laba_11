from arrays import Array2D


class GreyScaleImage:
    def __init__(self, num_rows, num_cols):
        self._grid = Array2D(num_rows, num_cols)
        self.clear(0)

    def width(self):
        return self._grid.num_rows()

    def height(self):
        return self._grid.num_cols()

    def clear(self, value):
        assert 0 <= value <= 255, "Value has to be greater than 0 and lower than 255"
        for i in range(self._grid.num_rows()):
            for j in range(self._grid.num_cols()):
                self._grid[(i, j)] = value

    def getitem(self, row, col):
        return self._grid[(row, col)]

    def setitem(self, row, col, value):
        self._grid[(row, col)] = value

    def __str__(self):
        st = ""
        for i in range(self.width()):
            for j in range(self.height()):
                st += str(self._grid[(i, j)])
            st += "\n"
        return st

if __name__ == "__main__":
    qw = GreyScaleImage(10, 10)
    print(qw)
    qw.clear(5)
    print(qw)
    qw.setitem(3, 4, 8)
    print(qw)
    print(qw.height())
    print(qw.width())
    print(qw.getitem(3,4))


