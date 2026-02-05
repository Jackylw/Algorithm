# https://www.nowcoder.com/practice/ff77cca50f5d4793a14a94f141de0af3
from typing import List


class Solution:
    def commaTransformer(self , a: List[int]) -> str:
        return ",".join(map(str, a))