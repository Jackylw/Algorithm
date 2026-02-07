# https://ac.nowcoder.com/acm/contest/120563/J
t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    for _ in range(q):
        x = int(input())
        deth = x.bit_length() - 1
        # 层范围
        level_start = 1 << deth
        level_end = min((level_start << 1) - 1, n)
        ans = level_end - level_start + 1
        print(ans)
