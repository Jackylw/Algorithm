# https://www.nowcoder.com/practice/91fd90931d2847b5855075c11cf90d08
n = int(input())
ans = 0
while n > 0:
    ans += n % 10
    n //= 10
print(ans)
