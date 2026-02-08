# https://www.nowcoder.com/practice/8d6a87b1e5314c0387dad5728dcc05be
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        s_map = {}
        t_map = {}
        for s in ransomNote:
            s_map[s] = s_map.get(s, 0) + 1
        for t in magazine:
            t_map[t] = t_map.get(t, 0) + 1
        for val, count in s_map.items():
            if t_map.get(val, 0) < count:
                return False
        return True
