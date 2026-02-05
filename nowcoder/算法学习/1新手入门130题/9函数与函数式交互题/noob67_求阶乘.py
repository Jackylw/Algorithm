# https://www.nowcoder.com/practice/d7f7e5ccdd1a4262b1f705de9911705f
class Solution:
    def factorialOfN(self, n: int) -> int:
        ans = 1
        for i in range(1, n + 1):
            ans = (ans * i) % (10 ** 9 + 7)
        return ans

