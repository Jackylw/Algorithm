# https://www.nowcoder.com/practice/47ee4c040f1648fc9ef7732d35402676
T = int(input())
for i in range(T):
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    S = cnt = 0
    for a in A:
        if a >= k:
            S += a
        if a == 0 and S >= 1:
            S -= 1
            cnt += 1
    print(cnt)
