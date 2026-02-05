# https://www.nowcoder.com/practice/f86fa2221c094b3d8d1fc79bae450d96
t = int(input())

for _ in range(t):
    s = input()
    stack = []
    for c in s:
        while True:
            if not stack:
                stack.append(c)
                break
            if c == 'o' and stack[-1] == 'o':
                stack.pop()
                c = 'O'
            elif c == 'O' and stack[-1] == 'O':
                stack.pop()
                break
            else:
                stack.append(c)
                break
    print(''.join(stack))
