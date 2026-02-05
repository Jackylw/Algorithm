# https://www.nowcoder.com/practice/aa08dec2eed24c629a7100e677144edd
class Solution:
    def firstSpeed(self, M: float, r: float) -> float:
        # v = sqrt(GM/r)
        return ((M * 6.67e-11) / r) ** 0.5

