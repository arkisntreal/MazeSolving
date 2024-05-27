from graphics import Window, Line, Point

class Cell:
    def __init__(self, window = None):
        self._win = window
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self.top_wall = True
        self.right_wall = True
        self.bottom_wall = True
        self.left_wall = True
        self.visited = False

    def draw(self, x1: int, y1: int, x2: int, y2: int):
        if (self._win == None):
            return

        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        top_line = Line(Point(x1, y1), Point(x2, y1))
        right_line = Line(Point(x2, y1), Point(x2, y2))
        bottom_line = Line(Point(x2, y2), Point(x1, y2))
        left_line = Line(Point(x1, y2), Point(x1, y1))

        if (self.top_wall == True):
            self._win.draw_line(top_line, "black")
        else: 
            self._win.draw_line(top_line, "white")

        if (self.right_wall == True):
            self._win.draw_line(right_line, "black")
        else: 
            self._win.draw_line(right_line, "white")

        if (self.bottom_wall == True):
            self._win.draw_line(bottom_line, "black")
        else: 
            self._win.draw_line(bottom_line, "white")

        if (self.left_wall == True):
            self._win.draw_line(left_line, "black")
        else: 
            self._win.draw_line(left_line, "white")
        

    def draw_move(self, to_cell, undo = False):
        color = "red"
        if undo:
            color = "gray"

        line = Line(Point(self._x1 + (self._x2 - self._x1) / 2, self._y1 + (self._y2 - self._y1) / 2),
                    Point(to_cell._x1 + (to_cell._x2 - to_cell._x1) / 2, to_cell._y1 + (to_cell._y2 - to_cell._y1) / 2))
        self._win.draw_line(line, color)
