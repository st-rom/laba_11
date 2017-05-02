from arrays import Array2D

class LifeGrid:
    """
    Implements the LifeGrid ADT for use with the Game of Life.
    """
    # Defines constants to represent the cell states.
    DEAD_CELL = 0
    LIVE_CELL = 1

    # Neighbours
    NEIGHBOURS = [(1, 1), (2, 1), (2, 2), (3, 6), (2, 5)]


    def __init__(self, num_rows, num_cols):
        """
        Creates the game grid and initializes the cells to dead.

        :param num_rows: the number of rows.
        :param num_cols: the number of columns.
        """
        # Allocates the 2D array for the grid.
        self._grid = Array2D(num_rows, num_cols)
        # Clears the grid and set all cells to dead.
        self.configure(list())

    def num_rows(self):
        """
        Returns the number of rows in the grid.

        :return: the number rows in the grid.
        """
        return self._grid.num_rows()

    def num_cols(self):
        """
        Returns the number of columns in the grid.

        :return:Returns the number of columns in the grid. 
        """
        return  self._grid.num_cols()

    def configure(self, coord_list):
        """
        Configures the grid to contain the given live cells.
        
        :param coord_list: 
        :return: 
        """
        self._grid.clear(self.DEAD_CELL)
        for i, j in coord_list:
            self.set_cell(i, j)

    def is_live_cell(self, row, col):
        """
        Does the indicated cell contain a live organism?
        
        :param row: row of the cell.
        :param col: column of the cell.
        :return: the result of check.
        """
        return self._grid[(row, col)] == self.LIVE_CELL

    def clear_cell(self, row, col):
        """
        Clears the indicated cell by setting it to dead.

        :param row: row of the cell.
        :param col: column of the cell.
        """
        self._grid[(row, col)] = self.DEAD_CELL


    def set_cell(self, row, col):
        """
        Sets the indicated cell to be alive.

        :param row: row of the cell.
        :param col: column of the cell.
        """
        self._grid[(row, col)] = self.LIVE_CELL


    def num_live_neighbors(self, row, col):
        """
        Returns the number of live neighbors for the given cell.

        :param row: row of the cell.
        :param col: column of the cell.
        :return: 
        """
        res = 0
        for i, j in self.NEIGHBOURS:
            new_row = row + i
            new_col = col + j
            if 0 <= new_row < self.num_rows() and 0 <= new_col < self.num_cols():
                res += self.is_live_cell(new_row, new_col)
        return res

    def __str__(self):
        s = ""#@$
        for i in range(self.num_rows()):
            for j in range(self.num_cols()):
                if self._grid[(i, j)] == self.LIVE_CELL:
                    s += "@"
                else:
                    s += "$"
            s += "\n"
        return s

if __name__ == "__main__":
    lg = LifeGrid(10, 10)
    print(lg)
    