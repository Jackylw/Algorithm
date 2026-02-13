# https://ac.nowcoder.com/acm/contest/120565/G
import sys

input = sys.stdin.readline


def f():
    opts = "0112233445142015320125410214530214510214102302142025101203201451451522302514203214510021454101002532"

    state = 0
    ans = []

    # 操作：值1->值2
    trans = {
        '0': {0: 3, 1: 2, 2: 1, 3: 0},
        '1': {0: 0, 1: 3, 2: 2, 3: 1},
        '2': {0: 1, 1: 0, 2: 3, 3: 2},
        '3': {0: 2, 1: 1, 2: 0, 3: 3},
        '4': {0: 1, 1: 2, 2: 3, 3: 0},
        '5': {0: 3, 1: 0, 2: 1, 3: 2}
    }
    for op in opts:
        state = trans[op][state]
        ans.append(str(state))

    print("".join(ans))


if __name__ == '__main__':
    f()
