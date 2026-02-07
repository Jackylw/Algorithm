# https://ac.nowcoder.com/acm/contest/120562/F
t = int(input())
for _ in range(t):
    n = int(input())
    k = 1
    while True:
        if (n << k) & n == 0:
            x = n << k
            y = x + n
            print(f"{x} {y}")
            break
        k += 1
