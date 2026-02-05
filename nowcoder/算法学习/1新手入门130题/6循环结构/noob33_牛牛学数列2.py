# https://www.nowcoder.com/practice/fc72951f52984f3abd286d82eeffacba
n = int(input())
ans = 0
for i in range(1, n + 1):
    ans += 1 / i
print(ans)
