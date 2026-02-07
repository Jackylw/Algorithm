# https://ac.nowcoder.com/acm/contest/120563/B
from math import gcd

t = int(input())
for _ in range(t):
    ans = []
    n = int(input())
    a = list(map(int, input().split()))
    found = False
    for i in range(n):
        for j in range(i + 1, n):
            if gcd(a[i], a[j]) > 1:
                ans.append(a[i])
                ans.append(a[j])
                found = True
                break
        if found:
            break
    if found:
        print(' '.join(map(str, ans)))
    else:
        print("-1")