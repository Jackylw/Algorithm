# https://www.nowcoder.com/practice/1bcdd78060e54812a9c47ebe40c6af65
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b


def get_distance(P, L):
    x0, y0 = P.x, P.y
    x1, y1 = L.point_a.x, L.point_a.y
    x2, y2 = L.point_b.x, L.point_b.y

    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    distance = abs(A * x0 + B * y0 + C) / math.sqrt(A * A + B * B)
    return distance
