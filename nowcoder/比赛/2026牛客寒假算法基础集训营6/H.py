import sys

input = sys.stdin.readline


def f():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    dp = [0]

    for i in range(n):
        states = set()
        for x in dp:
            states.add(max(0, x - a[i]))
            states.add(x ^ b[i])
        dp = list(states)

    print(max(dp))


if __name__ == '__main__':
    f()
