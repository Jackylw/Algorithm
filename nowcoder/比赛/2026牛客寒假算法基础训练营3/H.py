# https://ac.nowcoder.com/acm/contest/120563/H
xa, ya = map(int, input().split())
xb, yb = map(int, input().split())
C = xa * yb - xb * ya
D = ya - yb
if D != 0:
    x = (4 - C) / D
    print(x)
else:
    if abs(C) == 4:
        print("0")
    else:
        print("no answer")