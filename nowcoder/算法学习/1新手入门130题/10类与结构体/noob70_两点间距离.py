# https://www.nowcoder.com/practice/94712d6f654143379f8ea5847d9d6225
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution:
    def calculateDistance(self, point_A: Point, point_B: Point) -> float:
        return ((point_A.x - point_B.x) ** 2 + (point_A.y - point_B.y) ** 2) ** 0.5
