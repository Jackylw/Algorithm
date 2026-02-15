import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline


def f():
    n, m, l = map(int, input().split())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))

    gaps = []
    pos = 0
    for i in range(n):
        pos += X[i]
        gaps.append(pos)

    feet_left = 0
    feet_right = l

    def check_step():
        # 使用二分查找定位脚掌范围内的缝隙
        left_idx = bisect_right(gaps, feet_left)  # 第一个大于 feet_left 的缝隙
        right_idx = bisect_left(gaps, feet_right)  # 第一个不小于 feet_right 的缝隙

        # 如果存在缝隙在 (feet_left, feet_right) 范围内
        return left_idx < right_idx or (left_idx < len(gaps) and feet_left < gaps[left_idx] < feet_right)

    # 检查初始位置
    if check_step():
        print("YES")
        return

    # 模拟 m 步
    for i in range(m):
        feet_left += Y[i]
        feet_right += Y[i]

        if check_step():
            print("YES")
            return

    print("NO")


if __name__ == '__main__':
    f()
