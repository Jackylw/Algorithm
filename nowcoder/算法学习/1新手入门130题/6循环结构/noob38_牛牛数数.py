# https://www.nowcoder.com/practice/03a3cc96fa4847b387bf58bb800d67cf
n = int(input())


def f(n):
    str_n = str(n)
    if '4' in str_n or n % 4 == 0:
        return False
    return True

for i in range(1, n + 1):
    if f(i):
        print(i)