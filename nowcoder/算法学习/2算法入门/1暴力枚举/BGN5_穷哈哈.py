# https://www.nowcoder.com/practice/5b3184b233f34fb39a7f259ae82eb42c?tpId=385&tqId=11104909&channelPut=tracker1
import sys

input = sys.stdin.readline


def solve():
    n = int(input())
    s = input().strip()
    ans = 0
    cur_num = 0
    last_chr = None
    for c in s:
        if c not in ['a', 'h']:
            cur_num = 0
            last_chr = None
        else:
            # 首字母
            if last_chr is None:
                cur_num += 1
                last_chr = c
            # 交替
            elif c != last_chr:
                cur_num += 1
                last_chr = c
            # 与上一个字母相同
            else:
                cur_num = 1
                last_chr = c
        ans = max(ans, cur_num)
    print(ans)


if __name__ == '__main__':
    solve()
