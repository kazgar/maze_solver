from maze_parts import Line, Point

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self._visited = False
        
    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        
        left_wall = Line(Point(x1, y2), Point(x1, y1))
        if self.has_left_wall:
            self._win.draw_line(left_wall)
        elif not self.has_left_wall:
            self._win.draw_line(left_wall, "white")

        right_wall = Line(Point(x2, y1), Point(x2, y2))
        if self.has_right_wall:
            self._win.draw_line(right_wall)
        elif not self.has_right_wall:
            self._win.draw_line(right_wall, "white")
        
        top_wall = Line(Point(x1, y1), Point(x2, y1))
        if self.has_top_wall:
            self._win.draw_line(top_wall)
        elif not self.has_top_wall:
            self._win.draw_line(top_wall, "white")

        bottom_wall = Line(Point(x1, y2), Point(x2, self._y2))
        if self.has_bottom_wall:
            self._win.draw_line(bottom_wall)
        elif not self.has_bottom_wall:
            self._win.draw_line(bottom_wall, "white")

    def draw_move(self, to_cell, undo=False):
        color = "red"
        if undo:
            color = "gray"

        start_center_x = abs(self._x1 + self._x2) // 2
        start_centery_y = abs(self._y1 + self._y2) // 2
        
        destination_center_x = abs(to_cell._x1 + to_cell._x2) // 2
        destination_center_y = abs(to_cell._y1 + to_cell._y2) // 2

        line = Line(Point(start_center_x, start_centery_y), Point(destination_center_x, destination_center_y))
        self._win.draw_line(line, fill_color=color)