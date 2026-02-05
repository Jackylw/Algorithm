# https://www.nowcoder.com/practice/f334a81b22654efc8d7a67e31f60de50
class Solution:
    def predictVictory(self, s: str) -> str:
        d = s.count('D')
        r = s.count('R')
        if d > r:
            return 'Dark'
        elif r > d:
            return 'Red'
        else:
            if s[0] == 'R':
                return 'Red'
            else:
                return 'Dark'
