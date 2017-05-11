from arrays import Array2D


class GreyScaleImage:
    """
    Implements GreyScaleImage ADT for use in editing images
    """
    def __init__(self, num_rows, num_cols):
        """
        Creates the grid and initiates all cells to 0

        :param num_rows: number of rows
        :param num_cols: number of columns
        """
        self._grid = Array2D(num_rows, num_cols)
        self.clear(0)

    def width(self):
        """
        Returns the number of rows in the grid.

        :return: returns the number of rows in the grid.
        """
        return self._grid.num_rows()

    def height(self):
        """
        Returns the number of columns in the grid.

        :return: returns the number of columns in the grid.
        """
        return self._grid.num_cols()

    def clear(self, value):
        """
        Sets all cells in grid to value
        :param value: number higher than 0 and lower than 255
        """
        assert 0 <= value <= 255, "Value has to be greater than 0 and lower than 255"
        for i in range(self._grid.num_rows()):
            for j in range(self._grid.num_cols()):
                self._grid[(i, j)] = value

    def getitem(self, row, col):
        """
        Gets the value of the entered cell

        :param row: number of row
        :param col: number of column
        :return: the value of cell
        """
        return self._grid[(row, col)]

    def setitem(self, row, col, value):
        """
        Sets the cell to entered value

        :param row: number of row
        :param col: number of column
        :param value: number to which cell will be set
        :return:
        """
        self._grid[(row, col)] = value

    def __str__(self):
        """
        Creates string from the grid
        """
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
    print(qw.getitem(3, 4))
