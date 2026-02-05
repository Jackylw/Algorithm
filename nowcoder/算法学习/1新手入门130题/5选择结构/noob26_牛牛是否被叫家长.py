# https://www.nowcoder.com/practice/cc896ffd90d34c7faa318b04e87adf11
a, b, c = map(int, input().split())
avg = (a + b + c) / 3
if avg >= 60:
    print("NO")
else:
    print("YES")