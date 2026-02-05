# https://www.nowcoder.com/practice/1e683db4a34442098fb642d514bd0794
from typing import List


class Solution:
    def countLongestSubwayTime(self, t: List[int], s: List[int], x: int, y: int) -> int:
        ans = 0
        # 计算等待时间
        ans += sum(s[x - 1:y])
        # 计算行程时间
        ans += sum(t[x - 1:y - 1])
        return ans
