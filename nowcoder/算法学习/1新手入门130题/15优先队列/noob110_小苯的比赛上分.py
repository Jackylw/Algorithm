# https://www.nowcoder.com/practice/f5c52183dfb148489321f881239216c1
import heapq

n, m = map(int, input().split())
a = list(map(int, input().split()))
max_rating = max(a)
b = list(map(int, input().split()))
heapq.heapify(a)
for b_i in b:
    min_rating = heapq.heappop(a)
    new_rating = min_rating + b_i
    heapq.heappush(a, new_rating)
    max_rating = max(max_rating, new_rating)
    print(max_rating)
