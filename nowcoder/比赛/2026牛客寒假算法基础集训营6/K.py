import sys

input = sys.stdin.readline


def f():
    ans = []
    t = int(input())
    for _ in range(t):
        m, n, z = map(int, input().split())
        d = z % (m + n)
        # 刚好为 0，恰好 1 号满足
        if d == 0:
            ans.append(1)
            continue
        if d <= m:
            ans.append(0)
        else:
            ans.append(1)
    print("".join(map(str, ans)))


if __name__ == '__main__':
    f()
