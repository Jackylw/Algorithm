# https://www.nowcoder.com/practice/73e0552b78474a9086781e47f4e01d73?tpId=385&tqId=11104909&channelPut=tracker1
import sys

input = sys.stdin.readline


def solve():
    n = int(input())
    num6 = n // 6
    num8 = n // 8
    if n < 8 and n != 6 or n % 2 == 1:
        print(-1)
        return
    for i in range(num6 + 1):
        for j in range(num8 + 1):
            if 6 * i + 8 * j == n:
                print(i + j)
                return
    print(-1)


if __name__ == '__main__':
    solve()
