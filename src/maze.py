from cell import Cell
import time
import random

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        if seed:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls(0, 0)
        self._reset_cells_visited()
       
    def _create_cells(self):
        if self._num_rows < 1 or self._num_cols < 1:
            raise ValueError("number of rows and number of columns have to be at least 1")
        for i in range(self._num_cols):
            self._cells.append([])
            for j in range(self._num_rows):
                self._cells[i].append(Cell(self._win))

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        cell = self._cells[i][j]
        left_x = self._x1 + (j * self._cell_size_x)
        right_x = left_x + self._cell_size_x
        top_y = self._y1 + (i * self._cell_size_y)
        bot_y = top_y + self._cell_size_y
        cell.draw(left_x, top_y, right_x, bot_y)
        self._animate()
    
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        i, j = self._num_cols - 1, self._num_rows - 1 
        self._cells[i][j].has_bottom_wall = False
        self._draw_cell(i, j)
        
    def _break_walls(self, i, j):
        self._cells[i][j]._visited = True
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while True:
            neighbors = []
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < self._num_cols and 0 <= nj < self._num_rows and self._cells[ni][nj]._visited == False:
                    neighbors.append((ni, nj))

            if not neighbors:
                self._draw_cell(i, j)
                return
            
            i2, j2 = random.choice(neighbors)
            
            if i2 > i:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i2][j2].has_top_wall = False
            elif i2 < i:
                self._cells[i][j].has_top_wall = False
                self._cells[i2][j2].has_bottom_wall = False
            elif j2 > j:
                self._cells[i][j].has_right_wall = False
                self._cells[i2][j2].has_left_wall = False
            else:
                self._cells[i][j].has_left_wall = False
                self._cells[i2][j2].has_right_wall = False
            
            self._break_walls(i2, j2)
            

    def _reset_cells_visited(self):
        for column in self._cells:
            for cell in column:
                cell._visited = False

    '''
    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        visited_cells = []
        pass
    '''
