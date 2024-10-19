import unittest
from maze import Maze
from maze_parts import Window

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_empty_maze(self):
        win = Window(800, 600)

        num_cols = 0
        num_rows = 0

        try:
            m1 = Maze(0, 0, num_cols, num_rows, 10, 10)
            raise ValueError("Maze with 0 rows and 0 columns created")
        except:
            return 0
        
    def test_rows_diff_columns(self):
        win = Window(800, 600)

        num_rows = 1
        num_cols = 12

        m1 = Maze(0, 0, num_rows=num_rows, num_cols=num_cols, cell_size_x=10, cell_size_y=10)
        m2 = Maze(0, 0, num_rows=num_cols, num_cols=num_rows, cell_size_x=10, cell_size_y=10)

        self.assertNotEqual(
            m1,
            m2
        )

    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall,
            False,
        )

if __name__ == "__main__":
    unittest.main()