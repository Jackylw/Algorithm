# https://www.nowcoder.com/practice/f043b2390788458db7762300911e30df
from typing import List


class Solution:
    def dotTime(self, vector1: List[int], vector2: List[int]) -> int:
        lst = zip(vector1, vector2)
        ans = 0
        for num1, num2 in lst:
            ans += num1 * num2
        return ans
