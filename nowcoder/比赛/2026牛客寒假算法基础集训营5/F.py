import sys

input = sys.stdin.readline


def f():
    t = int(input())
    for _ in range(t):
        n, a, b = map(int, input().split())

        ans = 0

        # 核心思路：
        # 物品有三种：
        # 1. "qcjjkkt" (长度 7, 价值 a)
        # 2. "td" (长度 2, 价值 b)
        # 3. "qcjjkktd" (长度 8, 价值 a+b) -> 由 7 和 2 组合而成，省 1 长度
        # 结论：如果同时存在独立的 7 和 2，一定可以合并成 8 (更优)。
        # 因此，最优解中不可能同时存在 "qcjjkkt" 和 "td"。
        # 情况仅限于：
        # A. 只用 8 和 2
        # B. 只用 8 和 7

        # 情况 A: 只使用 "qcjjkktd" (8) 和 "td" (2)
        # 由于 8 是 2 的倍数，只需比较两种极端情况
        
        # A1: 优先填 8，剩余填 2
        cnt8 = n // 8
        rem = n % 8
        ans = max(ans, cnt8 * (a + b) + (rem // 2) * b)
        
        # A2: 全部填 2 (如果 4*b > a+b，则单位长度价值 2 更高)
        ans = max(ans, (n // 2) * b)

        # 情况 B: 只使用 "qcjjkktd" (8) 和 "qcjjkkt" (7)
        # 7 和 8 互质，不能简单贪心，需要枚举边界
        
        # B1: 枚举少量的 7 (假设 8 更优，但可能需要配几个 7 填缝)
        for i in range(9):  # 7*8=56，周期很小，枚举到 8 足够
            if i * 7 > n:
                break
            rem = n - i * 7
            cnt8 = rem // 8
            ans = max(ans, i * a + cnt8 * (a + b))
            
        # B2: 枚举少量的 8 (假设 7 更优，但可能需要配几个 8 填缝)
        for i in range(9):
            if i * 8 > n:
                break
            rem = n - i * 8
            cnt7 = rem // 7
            ans = max(ans, i * (a + b) + cnt7 * a)

        print(ans)


if __name__ == '__main__':
    f()
