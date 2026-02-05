# https://www.nowcoder.com/practice/2b2dc309c15f4b19949a03455ff3277c
from typing import List


class Solution:
    def crossTimes(self, vector1: List[int], vector2: List[int]) -> List[int]:
        ax, ay, az = vector1
        bx, by, bz = vector2
        cx = ay * bz - az * by
        cy = az * bx - ax * bz
        cz = ax * by - ay * bx
        return [cx, cy, cz]
