# https://www.nowcoder.com/practice/396cdc45427847d199c7e279303692bd
class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point_a=None, point_b=None):
        self.point_A = point_a if point_a is not None else Point()
        self.point_B = point_b if point_b is not None else Point()


def find_meeting_point(line_A, line_B):
    # 直线通过两点 (x1,y1)-(x2,y2) 的一般式: a x + b y + c = 0
    # a = y1 - y2, b = x2 - x1, c = x1*y2 - x2*y1
    x1, y1 = line_A.point_A.x, line_A.point_A.y
    x2, y2 = line_A.point_B.x, line_A.point_B.y
    a1 = y1 - y2
    b1 = x2 - x1
    c1 = x1 * y2 - x2 * y1

    x3, y3 = line_B.point_A.x, line_B.point_A.y
    x4, y4 = line_B.point_B.x, line_B.point_B.y
    a2 = y3 - y4
    b2 = x4 - x3
    c2 = x3 * y4 - x4 * y3

    d = a1 * b2 - a2 * b1
    if abs(d) < 10e-6:
        return Point(-1, -1)  # 平行或重合：按题意返回 -1 -1

    x = (b1 * c2 - b2 * c1) / d
    y = (c1 * a2 - c2 * a1) / d
    return Point(x, y)


def main():
    data = list(map(float, input().split()))
    data.extend(list(map(float, input().split())))
    A = Point(data[0], data[1])
    B = Point(data[2], data[3])
    C = Point(data[4], data[5])
    D = Point(data[6], data[7])
    AB = Line(A, B)
    CD = Line(C, D)
    ans = find_meeting_point(AB, CD)
    print(f"{ans.x:.6f} {ans.y:.6f}")


if __name__ == "__main__":
    main()
