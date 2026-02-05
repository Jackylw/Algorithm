# https://www.nowcoder.com/practice/57260c08eaa44feababd05b328b897d7
s = input()
stack = []
for char in s:
    if char == '[':
        stack.append(char)
    elif char == ']':
        if stack and stack[-1] == '[':
            stack.pop()
        else:
            print("false")
            exit(0)
    elif char == '(':
        stack.append(char)
    elif char == ')':
        if stack and stack[-1] == '(':
            stack.pop()
        else:
            print("false")
            exit()
if stack:
    print("false")
else:
    print("true")
