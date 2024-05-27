from cell import Cell
import random
import time

class Maze:
    def __init__(self, x1, y1, rows_num, cols_num, cell_size_x, cell_size_y, win = None, seed = None):
        self._x1 = x1
        self._y1 = y1
        self._rows_num = rows_num
        self._cols_num = cols_num
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._seed = seed
        self._cells = [[Cell for i in range(self._cols_num)] for j in range(self._rows_num)]

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self._rows_num):
            for j in range(self._cols_num):
                self._cells[i][j] = Cell(self._win)

        for i in range(self._rows_num):
            for j in range(self._cols_num):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if (self._win == None):
            return

        x = self._x1 + self._cell_size_x * i
        y = self._y1 + self._cell_size_y * j

        self._cells[i][j].draw(x, y, x + self._cell_size_x, y + self._cell_size_y)
        self._animate()
        
    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].left_wall = False
        self._draw_cell(0, 0)
        self._cells[self._rows_num - 1][self._cols_num - 1].right_wall = False
        self._draw_cell(self._rows_num - 1, self._cols_num - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while (True):
            possible_cells = []

            #   Top is possible
            if (j >= 1 and self._cells[i][j - 1].visited == False):
                    possible_cells.append([i, j - 1])
            #   Right is possible
            if (i < self._rows_num - 1 and self._cells[i + 1][j].visited == False):
                    possible_cells.append([i + 1, j])
            #   Bottom is possible
            if (j < self._cols_num - 1 and self._cells[i][j + 1].visited == False):
                    possible_cells.append([i, j + 1])
            #   Left is possible
            if (i >= 1 and self._cells[i - 1][j].visited == False):
                    possible_cells.append([i - 1, j])

            if (len(possible_cells) == 0):
                self._draw_cell(i, j)
                return
            
            #   Choose direction at random
            direction = random.randrange(len(possible_cells))
            next_cell = possible_cells[direction]
            
            #   Top will become a path
            if (next_cell[1] == j - 1):
                 self._cells[i][j].top_wall = False
                 self._cells[i][j - 1].bottom_wall = False
            #   Right will become a path
            if (next_cell[0] == i + 1):
                 self._cells[i][j].right_wall = False
                 self._cells[i + 1][j].left_wall = False
            #   Bottom will become a path
            if (next_cell[1] == j + 1):
                 self._cells[i][j].bottom_wall = False
                 self._cells[i][j + 1].top_wall = False
            #   Left will become a path
            if (next_cell[0] == i - 1):
                 self._cells[i][j].left_wall = False
                 self._cells[i - 1][j].right_wall = False

            self._break_walls_r(next_cell[0], next_cell[1])

    def _reset_cells_visited(self):
        for i in range(self._rows_num):
             for j in range(self._cols_num):
                  self._cells[i][j].visited = False

    def _solve_r(self, i, j) -> bool:
        self._animate()
        self._cells[i][j].visited = True

        if ([i, j] == [self._rows_num - 1, self._cols_num - 1]):
            return True
        
        #   Top
        if (self._cells[i][j].top_wall == False and self._cells[i][j - 1].visited == False):
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1) == True:
                return True
            self._cells[i][j].draw_move(self._cells[i][j - 1], True)
        #   Right
        if (self._cells[i][j].right_wall == False and self._cells[i + 1][j].visited == False):
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j) == True:
                return True
            self._cells[i][j].draw_move(self._cells[i + 1][j], True)
        #   Bottom
        if (self._cells[i][j].bottom_wall == False and self._cells[i][j + 1].visited == False):
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1) == True:
                return True
            self._cells[i][j].draw_move(self._cells[i][j + 1], True)
        #   Left
        if (self._cells[i][j].left_wall == False and self._cells[i - 1][j].visited == False):
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j) == True:
                return True
            self._cells[i][j].draw_move(self._cells[i - 1][j], True)

        
        return False

    def solve(self) -> bool:
         return self._solve_r(0, 0)
