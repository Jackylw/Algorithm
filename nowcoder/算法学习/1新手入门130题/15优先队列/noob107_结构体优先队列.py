# https://www.nowcoder.com/practice/e3d68ce7184e4658b42740edd4308d51
import heapq

n = int(input())
heap = []
for _ in range(n):
    opts = list(map(int, input().split()))
    if opts[0] == 1:
        x, y, z = opts[1], opts[2], opts[3]
        total = x + y + z
        # 大根堆
        entry = (-total, -x, -y, -z)
        heapq.heappush(heap, entry)
    elif opts[0] == 2:
        if heap:
            best = heap[0]
            print(f"{-best[1]} {-best[2]} {-best[3]}")
    elif opts[0] == 3:
        if heap:
            heapq.heappop(heap)
