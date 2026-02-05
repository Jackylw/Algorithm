# https://www.nowcoder.com/practice/7d05171e7e0e4c6086be233769e01d94
from collections import Counter

N, C = map(int, input().split())
nums = list(map(int, input().split()))
counts = Counter(nums)
ans = 0
for j_val, j_count in counts.items():
    i_val = j_val + C
    if i_val in counts:
        i_count = counts[i_val]
        ans += j_count * i_count
print(ans)
