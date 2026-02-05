# https://www.nowcoder.com/practice/06a5336b64e3481fbbcc1f7d5cba548d
n, m = map(int, input().split())
s = input()
for _ in range(m):
    l, r, c1, c2 = map(str, input().split())
    for i in range(int(l) - 1, int(r)):
        if s[i] == c1:
            s = s[:i] + c2 + s[i + 1:]
print(s)
