from src.window import Window
from src.cell import Cell
import time, random

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win = None,
        seed = None
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cell_visited()

    def _create_cells(self):
        x1 = self._x1
        x2 = x1 + self._cell_size_x
        for i in range(self._num_cols):
            column = []
            y1 = self._y1
            y2 = y1 + self._cell_size_y
            for j in range(self._num_rows):
                cell = Cell(x1, x2, y1, y2, self._win)
                column.append(cell)     
                y1 += self._cell_size_y
                y2 = y1 + self._cell_size_y
            x1 += self._cell_size_x
            x2 = x1 + self._cell_size_x
            self._cells.append(column)
        
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)


    def _draw_cell(self, i, j):
        if self._win:
            self._cells[i][j].draw()
            self._animate()

    def _animate(self):
        if self._win:
            self._win.redraw()
            time.sleep(0.03)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols-1][self._num_rows -1].has_bottom_wall = False
        self._draw_cell(self._num_cols-1, self._num_rows -1)

    def _break_walls_r(self, i, j):
        # self._cells[i][j].visited = True
        # while True:
        #     to_visit = {}

        #     if i > 0 and not self._cells[i - 1][j].visited:
        #         to_visit[self._cells[i - 1][j]] = "left"

        #     if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
        #         to_visit[self._cells[i + 1][j]] = "right"

        #     if j > 0 and not self._cells[i][j - 1].visited:
        #         to_visit[self._cells[i][j - 1]] = "top"

        #     if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
        #         to_visit[self._cells[i][j + 1]] = "bottom"

            
        #     if len(to_visit) == 0:
        #         self._draw_cell(i, j)
        #         return

        #     direction_index = random.randrange(len(to_visit))
        #     to_cell_key = list(to_visit)[direction_index]
        #     direction = to_visit[to_cell_key]

        #     match direction:
        #         case "right":
        #             self._cells[i][j].has_right_wall = False
        #             to_cell_key.has_left_wall = False
        #             self._break_walls_r(i + 1, j)
        #         case "left":
        #             self._cells[i][j].has_left_wall = False
        #             self._cells[i][j].has_right_wall = False
        #             self._break_walls_r(i - 1, j)
        #         case "top":
        #             self._cells[i][j].has_top_wall = False
        #             to_cell_key.has_bottom_wall = False
        #             self._break_walls_r(i, j + 1)
        #         case "bottom":
        #             self._cells[i][j].has_bottom_wall = False
        #             to_cell_key.has_top_wall = False
        #             self._break_walls_r(i, j - 1)

        self._cells[i][j].visited = True
        while True:
            next_index_list = []

            # determine which cell(s) to visit next
            # left
            if i > 0 and not self._cells[i - 1][j].visited:
                next_index_list.append((i - 1, j))
            # right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))
            # up
            if j > 0 and not self._cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))
            # down
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))

            # if there is nowhere to go from here
            # just break out
            if len(next_index_list) == 0:
                self._draw_cell(i, j)
                return

            # randomly choose the next direction to go
            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list[direction_index]

            # knock out walls between this cell and the next cell(s)
            # right
            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            # left
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            # down
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            # up
            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            # recursively visit the next cell
            self._break_walls_r(next_index[0], next_index[1])

    def _reset_cell_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False

    def solve(self):
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        # self._animate()
        # self._cells[i][j].visted = True
        # if i == self._num_cols-1 and j == self._num_rows -1:
        #     return True
        
        # # right
        # if (
        #     i < self._num_cols - 1
        #     and not self._cells[i][j].has_right_wall 
        #     and not self._cells[i + 1][j].visited
        #     ):
        #     self._cells[i][j].draw_move(self._cells[i + 1][j])
        #     if not self._solve_r(i + 1, j):
        #         self._cells[i][j].draw_move(self._cells[i + 1][j], True)
        #     else:
        #         return True

        # # left
        # if (
        #     i > 0
        #     and not self._cells[i][j].has_left_wall 
        #     and not self._cells[i - 1][j].visited
        #     ):
        #     self._cells[i][j].draw_move(self._cells[i - 1][j])
        #     if not self._solve_r(i - 1, j):
        #         self._cells[i][j].draw_move(self._cells[i - 1][j], True)
        #     else:
        #         return True

        # # top
        # if (
        #     j < self._num_rows - 1
        #     and not self._cells[i][j].has_top_wall 
        #     and not self._cells[i][j + 1].visited
        #     ):
        #     self._cells[i][j].draw_move(self._cells[i][j + 1])
        #     if not self._solve_r(i, j + 1):
        #         self._cells[i][j].draw_move(self._cells[i][j + 1], True)
        #     else:
        #         return True

        # # bottom
        # if (
        #     j > 0
        #     and not self._cells[i][j].has_bottom_wall 
        #     and not self._cells[i][j - 1].visited
        #     ):
        #     self._cells[i][j].draw_move(self._cells[i][j - 1])
        #     if not self._solve_r(i, j - 1):
        #         self._cells[i][j].draw_move(self._cells[i][j - 1], True)
        #     else:
        #         return True
            
        # return False

        self._animate()

        # vist the current cell
        self._cells[i][j].visited = True

        # if we are at the end cell, we are done!
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True

        # move left if there is no wall and it hasn't been visited
        if (
            i > 0
            and not self._cells[i][j].has_left_wall
            and not self._cells[i - 1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)

        # move right if there is no wall and it hasn't been visited
        if (
            i < self._num_cols - 1
            and not self._cells[i][j].has_right_wall
            and not self._cells[i + 1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)

        # move up if there is no wall and it hasn't been visited
        if (
            j > 0
            and not self._cells[i][j].has_top_wall
            and not self._cells[i][j - 1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], True)

        # move down if there is no wall and it hasn't been visited
        if (
            j < self._num_rows - 1
            and not self._cells[i][j].has_bottom_wall
            and not self._cells[i][j + 1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)

        # we went the wrong way let the previous cell know by returning False
        return False
        
            

            
