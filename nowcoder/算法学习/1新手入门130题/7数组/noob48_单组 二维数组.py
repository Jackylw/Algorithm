# https://www.nowcoder.com/practice/4df606b6c3764d9c969f8759c8a4807b
n, m = map(int, input().split())
nums_sum = 0
for _ in range(n):
        nums_sum += sum(map(int, input().split()))
print(nums_sum)

