# https://www.nowcoder.com/practice/7f3c2ebfc3be442897393f7da5d021c8
import heapq

heap = []
n = int(input())
for _ in range(n):
    opts = list(map(str, input().split()))
    if opts[0] == '1':
        heapq.heappush(heap, opts[1])
    elif opts[0] == '2':
        print(heap[0])
    elif opts[0] == '3':
        heapq.heappop(heap)
