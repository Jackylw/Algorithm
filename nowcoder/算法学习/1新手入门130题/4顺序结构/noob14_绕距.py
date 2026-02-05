# https://www.nowcoder.com/practice/7a245fc6284f4139b4fb21de58e68483
from cmath import sqrt

x_1, y_1 = map(int, input().split())
x_2, y_2 = map(int, input().split())
d_e = sqrt((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2)
d_m = abs(x_1 - x_2) + abs(y_1 - y_2)
print(f"{abs(d_m - d_e):.6f}")
