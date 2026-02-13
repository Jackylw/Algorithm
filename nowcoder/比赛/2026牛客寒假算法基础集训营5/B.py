# https://ac.nowcoder.com/acm/contest/120565/B
import sys

input = sys.stdin.readline


def f():
    n, m = map(int, input().split())
    matrix = [['0'] * m for _ in range(n)]
    matrix[0][0] = '/'
    for i in range(n):
        for j in range(m):
            # 跳过第一个元素
            if i == 0 and j == 0:
                continue

            for dx, dy in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= dx < n and 0 <= dy < m and matrix[dx][dy] == '/':
                    matrix[i][j] = '\\'
                    break
                if 0 <= dx < n and 0 <= dy < m and matrix[dx][dy] == '\\':
                    matrix[i][j] = '/'
                    break
    for i in range(n):
        for j in range(m):
            print(matrix[i][j], end='')
        print()


if __name__ == '__main__':
    f()
