# https://www.nowcoder.com/practice/b10a7ac681e9429e89a6a510e5799647
from collections import deque

t = int(input())
in_queue = deque(list(map(int, input().split())))
tmp = []
out_queue = deque()
i = 0
while in_queue:
    target = t - i
    while in_queue and in_queue[0] != target:
        tmp.append(in_queue.popleft())
    if in_queue[0] == target:
        out_queue.append(in_queue.popleft())
        i += 1
# 处理剩余
while tmp:
    out_queue.append(tmp.pop())
print(' '.join(map(str, out_queue)))
