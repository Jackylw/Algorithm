# https://www.nowcoder.com/practice/4015c0d05e1f42028520494b7ecef2b8
from typing import List


class Solution:
    def countPeakPoint(self, a: List[int]) -> int:
        ans = 0
        n = len(a)
        for i in range(1, n - 1):
            if a[i - 1] < a[i] and a[i] > a[i + 1]:
                ans += 1 # 峰点
            if a[i] < a[i - 1] and a[i] < a[i + 1]:
                ans += 1 # 谷点
        return ans
