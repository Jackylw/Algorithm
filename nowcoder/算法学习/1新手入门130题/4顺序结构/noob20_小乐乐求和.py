# https://www.nowcoder.com/practice/ce0b2eacd3d04647831358c2876e44ff
n = int(input())

# 利用等差数列前n项和公式，时间复杂度降至o(1)
ans = n * (n + 1) // 2
print(ans)
