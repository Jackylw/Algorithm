# https://www.nowcoder.com/practice/f31371f27dcd4c90a8fd2902d3e4592c
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set(nums1)
        s2 = set(nums2)
        return sorted(s1 & s2)


print(Solution().intersection(nums1=[1, 1, 4], nums2=[5, 1, 4]))
