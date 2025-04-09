from src.window import Window
from src.line import Line
from src.point import Point

class Cell():
    def __init__(self, x1 : int, x2 : int, y1 : int, y2 : int, win : Window):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        self.__win = win
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited= False
    
    def draw(self):
        top_left = Point(self.__x1, self.__y1)
        top_right = Point(self.__x2, self.__y1)
        bottom_left = Point(self.__x1, self.__y2)
        bottom_right = Point(self.__x2, self.__y2)

        line = Line(top_left, bottom_left)
        self.line_draw_helper(line, self.has_left_wall)
        line = Line(top_right, bottom_right)
        self.line_draw_helper(line, self.has_right_wall)
        line = Line(top_left, top_right)
        self.line_draw_helper(line, self.has_top_wall)
        line = Line(bottom_left, bottom_right)
        self.line_draw_helper(line, self.has_bottom_wall)

    def get_center(self):
        width = max(self.__x1, self.__x2) - min(self.__x1, self.__x2)
        x_center = max(self.__x1, self.__x2) - (width / 2)
        height = max(self.__y1, self.__y2) - min(self.__y1, self.__y2)
        y_center = max(self.__y1, self.__y2) - (height / 2)
        return Point(x_center, y_center)
    
    def line_draw_helper(self, line, has_wall):
        if has_wall:
            self.__win.draw_line(line, "black")
        else:
            self.__win.draw_line(line, "white")

    
    def draw_move(self, to_cell, undo = False):
        line = Line(self.get_center(), to_cell.get_center())
        if undo:
            self.__win.draw_line(line, "gray")
        else:
            self.__win.draw_line(line, "red")

        


    
