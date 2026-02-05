# https://www.nowcoder.com/practice/e417cfe32c74416ca38247f619ddb322
from collections import deque

n, k, m = map(int, input().split())
q = deque(range(0, n))
# 调整队头为 k
for _ in range(k):
    q.append(q.popleft())
while len(q) > 1:
    # 循环将队头添加至队尾，到达m时删除队头
    for _ in range(m - 1):
        q.append(q.popleft())
    _ = q.popleft()
print(q[0])
