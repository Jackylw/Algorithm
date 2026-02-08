# https://www.nowcoder.com/practice/59426f49136349b0901cc1b70447bf4b
class Solution:
    def isCongruent(self, s: str, c: str) -> int:
        s_map = {}
        c_map = {}
        for s_i in s:
            s_map[s_i] = s_map.get(s_i, 0) + 1
        for c_i in c:
            c_map[c_i] = c_map.get(c_i, 0) + 1
        if s_map == c_map:
            return len(s)
        else:
            return -1
