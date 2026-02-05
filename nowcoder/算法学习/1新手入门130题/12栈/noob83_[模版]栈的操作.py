# https://www.nowcoder.com/practice/cdf02ea916454957b575585634e5773a
n = int(input())
stack = []
for _ in range(n):
    opt = list(input().split())
    if opt[0] == "push":
        stack.append(opt[1])
    elif opt[0] == "pop":
        if stack:
            stack.pop()
        else:
            print("Empty")
    elif opt[0] == "query":
        if stack:
            print(stack[-1])
        else:
            print("Empty")
    elif opt[0] == "size":
        print(len(stack))
