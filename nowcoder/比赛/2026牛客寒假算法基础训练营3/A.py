# https://ac.nowcoder.com/acm/contest/120563/A
from math import sqrt

n = int(input())
k = (-1 + sqrt(1 + 4 * n)) / 2
if k % 1 == 0:
    print("YES")
else:
    print("NO")
