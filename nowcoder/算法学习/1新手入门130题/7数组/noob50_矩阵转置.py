# https://www.nowcoder.com/practice/351b3d03e410496ab5a407b7ca3fd841
n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

# method1
for row in [list(a) for a in zip(*A)]:
    print(*row)

# method2
for i in range(m):
    for j in range(n):
        print(A[j][i], end=" ")
    print()