# https://www.nowcoder.com/practice/cbd0c91f821847a4bb1c5115405f6eda?tpId=385&tqId=10995371&channelPut=tracker1
import sys


def solve():
    a = list(map(int, sys.stdin.readline().split()))
    for idx, val in enumerate(a):
        if val == 1:
            return idx + 1
    return -1


if __name__ == '__main__':
    print(solve())
