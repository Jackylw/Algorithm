# https://www.nowcoder.com/practice/a88e9711f7b04369982bbe8902278ae4
import heapq

n = int(input())
heap = []
for _ in range(n):
    opts = list(map(int, input().split()))
    if opts[0] == 1:
        heapq.heappush(heap, opts[1])
    elif opts[0] == 2:
        print(heap[0])
    elif opts[0] == 3:
        heapq.heappop(heap)
