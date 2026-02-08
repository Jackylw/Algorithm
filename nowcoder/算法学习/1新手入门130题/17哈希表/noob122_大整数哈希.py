# https://www.nowcoder.com/practice/29f0cff8a69b4ab6a2f63fb7386defa3
n = int(input())
f = {}
total = 0
for i in range(1, n + 1):
    x, y = map(int, input().split())
    ans = f.get(x, 0)
    total = (total + i * ans) % (2 ** 64)
    f[x] = y
print(total)
