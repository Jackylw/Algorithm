# https://www.nowcoder.com/practice/5ab1b9690af047699e96c87dee65def4
T = int(input())


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


for i in range(T):
    n = int(input())
    if is_prime(n):
        print("Yes")
    else:
        print("No")
