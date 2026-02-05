# https://www.nowcoder.com/practice/f1b20bcca3d847bea0afcbffef1d4e69
class Solution:
    def judgeSolutions(self, a: int, b: int, c: int) -> bool:
        # 一元二次方程有解看 b ^ 2 - 4ac >= 0 即可
        return b * b - 4 * a * c >= 0

