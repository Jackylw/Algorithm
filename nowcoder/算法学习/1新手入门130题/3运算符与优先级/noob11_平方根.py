# https://www.nowcoder.com/practice/cd21e09482f24b03842f02ae3d403cad
from math import sqrt

n = int(input())

# method1
print(int(sqrt(n)))

# method2
ans = 0
while True:
    if ans ** 2 > n:
        print(ans - 1)
        break
    if ans ** 2 == n:
        print(ans)
        break
    ans += 1
