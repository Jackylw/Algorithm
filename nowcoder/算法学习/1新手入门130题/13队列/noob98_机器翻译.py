# https://www.nowcoder.com/practice/45ecfecd83104f37a685016361be504c
from collections import deque

m, n = map(int, input().split())
W = list(map(int, input().split()))
cache = deque()
ans = 0
for ch in W:
    if ch not in cache and len(cache) < m:
        ans += 1
        cache.append(ch)
    elif ch not in cache:
        cache.popleft()
        cache.append(ch)
        ans += 1
print(ans)
