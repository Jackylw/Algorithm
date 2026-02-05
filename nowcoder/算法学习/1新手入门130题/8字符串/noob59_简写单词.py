# https://www.nowcoder.com/practice/0cfa856bf0d649b88f6260d878f35bb4
lst = input().split()
ans = ''
for word in lst:
    ans += word[0].upper()
print(ans)