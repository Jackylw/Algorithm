# https://www.nowcoder.com/practice/42c2f0c1351e4a6689ff64eddaf97a37
class Solution:
    def decodeWangzai(self, password: str, n: int) -> str:
        ans = ''
        for i in password:
            ans += chr((ord(i) - ord('a') - n) % 26 + ord('a'))
        return ans