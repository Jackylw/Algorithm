# https://www.nowcoder.com/practice/12da4185c0bb45918cfdc3072e544069
q = int(input())
ans = []
for _ in range(q):
    opt = list(map(int, input().split()))
    if opt[0] == 1:
        ans.append(opt[1])
    elif opt[0] == 2:
        ans.pop()
    elif opt[0] == 3:
        print(ans[(opt[1])])
    elif opt[0] == 4:
        ans.insert(opt[1] + 1, opt[2])
    elif opt[0] == 5:
        ans.sort()
    elif opt[0] == 6:
        ans.sort(reverse=True)
    elif opt[0] == 7:
        print(len(ans))
    elif opt[0] == 8:
        print(' '.join(map(str, ans)))
