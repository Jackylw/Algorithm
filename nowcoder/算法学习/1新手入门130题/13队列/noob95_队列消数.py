# https://www.nowcoder.com/practice/48f6e451ff52440798067b77dc5ea95b
from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        j = 0  # 队列的索引
        ans = 0
        while tickets[k] > 0:
            if tickets[j] > 0:
                tickets[j] -= 1
                ans += 1
            j = (j + 1) % len(tickets)
        return ans


print(Solution().timeRequiredToBuy([1, 1, 4, 5, 1, 4], 2))
