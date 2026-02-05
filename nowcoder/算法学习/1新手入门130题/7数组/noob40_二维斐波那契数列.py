# https://www.nowcoder.com/practice/a1951ca9431646ff8f9bc6f6d24d1e0a
n, m = map(int, input().split())
Aij = [[0] * (m + 1) for i in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i == 1 and j == 1:
            Aij[i][j] = 1
        elif i <= 2 and j == 1:
            Aij[i][j] = Aij[i - 1][j]
        elif i == 1 and j <= 2:
            Aij[i][j] = Aij[i][j - 1]
        else:
            Aij[i][j] = Aij[i - 1][j] + Aij[i][j - 1]
print(Aij[n][m] % (10 ** 9 + 7))
