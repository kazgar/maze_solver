from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("Kazik's Maze Solver")
        self.__canvas = Canvas(self.__root, height=self.height, width=self.width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__is_running = True
        while self.__is_running:
            self.redraw()

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)
    
    def close(self):
        self.__is_running = False


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)


class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        
    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            wall = Line(Point(x1, y2), Point(x1, y1))
            self._win.draw_line(wall)
        if self.has_right_wall:
            wall = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(wall)
        if self.has_top_wall:
            wall = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(wall)
        if self.has_bottom_wall:
            wall = Line(Point(x1, y2), Point(x2, self._y2))
            self._win.draw_line(wall)

