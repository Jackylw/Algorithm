# https://www.nowcoder.com/practice/739afacabadd463d9b73b23514bb6d5d
from typing import List


class Solution:
    def stopAtWho(self, a: List[int], m: int) -> int:
        cur = 0
        for _ in range(m):
            cur = (cur - a[cur]) % len(a)
        return cur + 1


print(Solution().stopAtWho([2, 1, 4, 5, 2, 3], 3))
