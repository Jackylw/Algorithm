# https://www.nowcoder.com/practice/6f5d239c34a7429cb325a3d836abc342
T = int(input())
for i in range(T):
    n = int(input())
    A = list(map(int, input().split()))
    avg = sum(A) / n
    var = sum([(a - avg) ** 2 for a in A]) / n
    print(max(A) - min(A), f"{var:.3f}")
