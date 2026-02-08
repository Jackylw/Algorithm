# https://www.nowcoder.com/practice/c4a4f030ca374d9bb9df5c0bdf388626
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for idx, num in enumerate(nums):
            i = target - num
            if i in hashmap:
                return [hashmap[i], idx]
            hashmap[num] = idx
        return []
