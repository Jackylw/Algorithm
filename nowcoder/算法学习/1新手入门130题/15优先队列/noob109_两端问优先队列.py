# https://www.nowcoder.com/practice/da2887a3fd8549ad826c9cbdaa67f513
import heapq
from collections import defaultdict

max_heap = []
min_heap = []
counter = defaultdict(int)
n = int(input())
for _ in range(n):
    opts = list(map(int, input().split()))
    if opts[0] == 1:
        heapq.heappush(max_heap, -opts[1])
        heapq.heappush(min_heap, opts[1])
        counter[opts[1]] += 1  # 记录有效元素
    elif opts[0] == 2:
        # 延迟删除
        while min_heap and counter[min_heap[0]] == 0:
            heapq.heappop(min_heap)
        if min_heap:
            print(min_heap[0])
    elif opts[0] == 3:
        while max_heap and counter[-max_heap[0]] == 0:
            heapq.heappop(max_heap)
        if max_heap:
            print(-max_heap[0])
    elif opts[0] == 4:
        while min_heap and counter[min_heap[0]] == 0:
            heapq.heappop(min_heap)
        val = heapq.heappop(min_heap)
        counter[val] -= 1
    elif opts[0] == 5:
        while max_heap and counter[-max_heap[0]] == 0:
            heapq.heappop(max_heap)
        val = heapq.heappop(max_heap)
        counter[-val] -= 1
