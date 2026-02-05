# https://www.nowcoder.com/practice/28b2d9f2bf2c48de94a1297ed90e1732
n, x = map(int, input().split())
count = 0
for i in range(1, n + 1):
    count += str(i).count(str(x))
print(count)
