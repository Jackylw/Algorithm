# https://www.nowcoder.com/practice/8c6984f3dc664ef0a305c24e1473729e
n = int(input())
A = [[1] * i for i in range(1, n + 1)]
for i in range(2, n):
    for j in range(1, i):
        A[i][j] = A[i - 1][j - 1] + A[i - 1][j]

for row in A:
    print(*row)
