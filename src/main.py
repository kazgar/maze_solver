from window import Window, Point, Line

def main():
    win = Window(800, 600)

    p1 = Point(0, 0)
    p2 = Point(100, 100)
    p3 = Point(0, 300)
    p4 = Point(800, 300)

    line_to_draw = Line(p1, p2)
    line2 = Line(p3,p4)

    win.draw_line(line_to_draw, "red")
    win.draw_line(line2, "blue")

    win.wait_for_close()

main()