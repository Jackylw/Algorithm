# https://www.nowcoder.com/practice/7e094c0a3a9945b3bee8e1f3c9ea246a
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    print(a + b)