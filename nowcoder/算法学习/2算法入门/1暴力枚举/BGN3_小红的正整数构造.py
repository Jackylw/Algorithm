# https://www.nowcoder.com/practice/7aa37cbc28034fe5af562ec7e44d1e76?tpId=385&tqId=11104909&channelPut=tracker1
import sys

input = sys.stdin.readline


def solve():
    l, r, x = map(int, input().split())
    for num in range(l, r + 1):
        if num % x == 0:
            print(num)
            return
    print(-1)


if __name__ == '__main__':
    solve()
