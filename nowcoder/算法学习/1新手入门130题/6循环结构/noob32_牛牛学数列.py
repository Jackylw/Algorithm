# https://www.nowcoder.com/practice/0b97367cd2184c12a0e02f7c223aee11
n = int(input())
ans = 0
for i in range(1, n + 1):
    ans += i * (-1) ** (i - 1)
print(ans)