# https://www.nowcoder.com/practice/c8615a370bb24ce6b110c3d7151c3dfc
import bisect

n = int(input())
a = []
for _ in range(n):
    opts = list(map(int, input().split()))
    if opts[0] == 1:
        x = opts[1]
        pos = bisect.bisect_left(a, x)
        if pos < len(a) and a[pos] == x:
            print("Already Exist")
        else:
            bisect.insort(a, x)
    elif opts[0] == 2:
        x = opts[1]
        if not a:
            print("Empty")
        else:
            pos = bisect.bisect_left(a, x)  # a[pos] >= x,a[pos-1] < x
            candidates = []
            if pos < len(a):  # 检查 a[pos] 是否有效
                candidates.append((abs(a[pos] - x), a[pos]))  # 距离、值
            if pos > 0:  # 检查 a[pos-1] 是否有效
                candidates.append((abs(a[pos - 1] - x), a[pos - 1]))
            candidates.sort(key=lambda t: (t[0], t[1]))  # 先按距离排序，距离相同按值排序
            best_val = candidates[0][1]
            del_pos = bisect.bisect_left(a, best_val)
            del a[del_pos]
            print(best_val)
