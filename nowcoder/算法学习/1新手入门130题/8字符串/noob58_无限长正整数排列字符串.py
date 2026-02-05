# https://www.nowcoder.com/practice/82c92d2321bb4220a3006d52a95a8bdd
n = int(input())
s = ''
for i in range(1, n + 1):
    s += str(i)
print(s[n - 1])
