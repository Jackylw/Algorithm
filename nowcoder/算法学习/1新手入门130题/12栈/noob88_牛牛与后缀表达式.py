# https://www.nowcoder.com/practice/a1a4f178f6ff4188890e51da1cc8ce10
class Solution:
    def legalExp(self, str):
        num_list = []
        num = ""
        for c in str:
            if c.isdigit():
                num += c
            elif c == '#':
                if num:
                    num_list.append(int(num))
                    num = ""
            elif c in "-+*":
                if num:
                    num_list.append(int(num))
                    num = ""
                b = num_list.pop()
                a = num_list.pop()
                if c == '+':
                    num_list.append(a + b)
                elif c == '-':
                    num_list.append(a - b)
                elif c == '*':
                    num_list.append(a * b)
        return num_list[0]

s = input()
print(Solution().legalExp(s[1:-1]))
