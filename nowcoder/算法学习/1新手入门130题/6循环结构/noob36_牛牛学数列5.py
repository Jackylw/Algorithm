# https://www.nowcoder.com/practice/6db6674518a9456198c166bcd0d2aaa1
n = int(input())
if 1 <= n < 3:
    print(1)
else:
    ans = 0
    pre = 1
    cur = 1
    for i in range(3, n+1):
        ans = pre + cur
        pre = cur
        cur = ans
    print(ans)
