# https://www.nowcoder.com/practice/396cdc45427847d199c7e279303692bd
class Point:
    def __init__(self, A, B):
        self.x = A
        self.y = B

class Line:
    def __init__(self, A, B):
        self.point_A = A
        self.point_B = B

class Circle:
    def __init__(self, A, B):
        self.O = A
        self.r = B

def getDistance(circle, l):
    x0, y0 = circle.O.x, circle.O.y
    x1, y1 = l.point_A.x, l.point_A.y
    x2, y2 = l.point_B.x, l.point_B.y
    dx = x2 - x1
    dy = y2 - y1
    numerator = abs(dy * x0 - dx * y0 + x2 * y1 - y2 * x1)
    denominator = (dx * dx + dy * dy) ** 0.5
    d = numerator / denominator
    r = circle.r
    chord_length = 2.0 * (max(0.0, r * r - d * d)) ** 0.5
    return chord_length