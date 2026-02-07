# https://ac.nowcoder.com/acm/contest/120562/H
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    last_pos = {}
    total_val = 0
    for i in range(n):
        val = a[i]
        k = i + 1
        prev = last_pos.get(val, 0)
        last_pos[val] = k
        term1 = k - prev
        rem = n - k + 1
        term2 = rem * (rem + 1) // 2
        total_val += term1 * term2
    print(total_val)
