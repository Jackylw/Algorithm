# https://www.nowcoder.com/practice/d5f277427d9a4cd3ae60ea6c276dddfd
n, m = map(int, input().split())
A = [list(input()) for _ in range(n)]

count_matrix = [[0] * m for _ in range(n)]
directions = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1), (0, 1),
              (1, -1), (1, 0), (1, 1)]
for i in range(n):
    for j in range(m):
        if A[i][j] == '*':
            for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < m:
                        count_matrix[ni][nj] += 1

for i in range(n):
    for j in range(m):
        if A[i][j] == '*':
            count_matrix[i][j] = '*'

for line in count_matrix:
    print(''.join(map(str, line)))
