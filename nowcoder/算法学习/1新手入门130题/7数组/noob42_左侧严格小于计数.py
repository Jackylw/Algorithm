# https://www.nowcoder.com/practice/c5922c6cdd1445749bd42f586c422435
n = int(input())
A = list(map(int, input().split()))
B = []
for i in range(n):
    count = 0
    for j in range(0, i):
        if A[i] > A[j]:
            count += 1
    B.append(count)
print(*B)
