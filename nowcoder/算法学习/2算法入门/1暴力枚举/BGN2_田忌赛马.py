# https://www.nowcoder.com/practice/49d799f65a0749588e9cd7e6135a4a9a?tpId=385&tqId=11141550&channelPut=tracker1
import sys
from itertools import permutations

input = sys.stdin.readline


def solve():
    king = list(map(int, input().split()))
    tianji = list(map(int, input().split()))

    # 田忌赛马的精髓在于用特定的排列顺序去针对对手的固定顺序。
    # 由于只有3匹马，我们可以枚举田忌所有可能的出马顺序（3! = 6种）。

    can_win = False
    for p in permutations(tianji):
        wins = 0
        for i in range(3):
            if p[i] > king[i]:
                wins += 1
        if wins >= 2:
            can_win = True
            break

    if can_win:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    solve()
