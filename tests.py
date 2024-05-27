from maze import Maze
from cell import Cell
import unittest

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        rows_num = 7
        cols_num = 12
        m1 = Maze(0, 0, rows_num, cols_num, 10, 10)
        self.assertEqual(
            len(m1._cells),
            rows_num
        )
        self.assertEqual(
            len(m1._cells[0]),
            cols_num
        )

    def test_maze_create_cells_xxl(self):
        rows_num = 57
        cols_num = 25
        m1 = Maze(-57, 1999, rows_num, cols_num, 500, 500)
        self.assertEqual(
            len(m1._cells),
            rows_num
        )
        self.assertEqual(
            len(m1._cells[0]),
            cols_num
        )

    def test_maze_break_entrance_and_exit(self):
        rows_num = 7
        cols_num = 12
        m1 = Maze(0, 0, rows_num, cols_num, 10, 10)
        m1._break_entrance_and_exit()
        self.assertEqual(
            m1._cells[0][0].left_wall,
            False
        )
        self.assertEqual(
            m1._cells[rows_num - 1][cols_num - 1].right_wall,
            False
        )

    def test_maze_break_walls_r(self):
        rows_num = 7
        cols_num = 12
        m1 = Maze(0, 0, rows_num, cols_num, 10, 10, None, 5124312)
        m1._break_entrance_and_exit()
        m1._break_walls_r(rows_num - 1, cols_num - 1)
        m1._break_walls_r(0, 0)

    def test_maze_reset_cell_status(self):
        rows_num = 7
        cols_num = 12
        m1 = Maze(0, 0, rows_num, cols_num, 10, 10, None, 5124312)
        m1._break_entrance_and_exit()
        m1._break_walls_r(rows_num - 1, cols_num - 1)
        m1._break_walls_r(0, 0)
        m1._reset_cells_visited()

if __name__ == "__main__":
    unittest.main()
