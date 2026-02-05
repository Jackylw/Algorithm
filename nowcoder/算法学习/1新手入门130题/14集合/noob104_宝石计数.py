# https://www.nowcoder.com/practice/d7c20bd9aa094e35b465b566eec86cf2
from collections import Counter


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j = set(jewels)
        s = Counter(stones)
        ans = 0
        for val, count in s.items():
            if val in j:
                ans += count
        return ans
