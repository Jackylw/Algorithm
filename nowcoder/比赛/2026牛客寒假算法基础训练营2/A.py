# https://ac.nowcoder.com/acm/contest/120562/A
t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    if abs(a - b) >= 2 or abs(a - c) >= 2 or abs(b - c) >= 2:
        print("NO")
    else:
        print("YES")