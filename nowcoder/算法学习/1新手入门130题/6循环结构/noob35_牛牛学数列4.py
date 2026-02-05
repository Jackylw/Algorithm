# https://www.nowcoder.com/practice/586b114f52034688879342ba45779081
n = int(input())
ans = 0
for i in range(1, n + 1):
    cur_sum = i * (i + 1) // 2
    ans += cur_sum
print(ans)
