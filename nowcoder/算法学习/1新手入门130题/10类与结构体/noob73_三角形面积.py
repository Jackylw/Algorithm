# https://www.nowcoder.com/practice/52992a1ac2b842cc84d3fd3813b9566d
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


def get_area(T):
    x1, y1 = T.a.x, T.a.y
    x2, y2 = T.b.x, T.b.y
    x3, y3 = T.c.x, T.c.y
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)
