import unittest
from src.maze import Maze

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
    
    def test_maze_create_cells2(self):
        num_cols = 4
        num_rows = 3
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_entrance_and_exit(self):
        num_cols = 10
        num_rows = 7
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._cells[0][0].has_left_wall,
            False
        )
        self.assertEqual(
            m1._cells[0][1].has_left_wall,
            True
        )

        self.assertEqual(
            m1._cells[num_cols-1][num_rows-1].has_right_wall,
            False
        )
    
    def test_reset_visited(self):
        num_cols = 10
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._cells[4][4].visited,
            False
        )
        self.assertEqual(
            m1._cells[5][7].visited,
            False
        )


if __name__ == "__main__":
    unittest.main()