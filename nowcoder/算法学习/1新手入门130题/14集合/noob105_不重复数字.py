# https://www.nowcoder.com/practice/38532b5539164242b4252352be8749ab
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    s = set()
    ans = []
    for x in arr:
        if x not in s:
            s.add(x)
            ans.append(x)
        else:
            continue
    print(' '.join(map(str, ans)))
