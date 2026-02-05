# https://www.nowcoder.com/practice/0e8cfc82936048769af45967f3c4ef7e
L, M = map(int, input().split())
tree = [1] * (L + 1)
for _ in range(M):
    start, end = map(int, input().split())
    for i in range(start, end + 1):
        tree[i] = 0
print(sum(tree))
