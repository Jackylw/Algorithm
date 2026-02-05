# https://www.nowcoder.com/practice/293b9ddd48444fa493dd17da0feb192d
class Solution:
    def happynum(self, n: int) -> bool:
        def f(n):
            num = 0
            while n > 0:
                num += (n % 10) ** 2
                n //= 10
            return num

        hsy = set()
        while n not in hsy:
            hsy.add(n)
            n = f(n)
            if n == 1:
                return True
        return False


print(Solution().happynum(19))
print(Solution().happynum(111))
