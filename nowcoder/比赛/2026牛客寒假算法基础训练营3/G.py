# https://ac.nowcoder.com/acm/contest/120563/G
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    sum_a = sum(a)
    sum_b = sum(b)
    if sum_a == sum_b:
        print("1")
        continue
    elif sum_a > sum_b:
        diff = sum_a - sum_b
        a.sort(reverse=True)
        remove_val = 0
        count = 0
        for x in a:
            remove_val += x
            count += 1
            if remove_val >= diff:
                print(count)
                break
    else:
        diff = sum_b - sum_a
        b.sort(reverse=True)
        remove_val = 0
        count = 0
        for x in b:
            remove_val += x
            count += 1
            if remove_val >= diff:
                print(count)
                break
