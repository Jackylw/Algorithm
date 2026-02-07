# https://ac.nowcoder.com/acm/contest/120562/B
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    max_value = max(a)
    count_max = a.count(max_value)
    res = []
    if count_max % 2 != 0:
        for x in a:
            res.append('1' if x == max_value else '0')
    else:
        for x in a:
            res.append('1' if x < max_value else '0')
    print(''.join(res))