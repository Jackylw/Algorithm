# https://www.nowcoder.com/practice/b6c48ca948a74afaaf1bc5b5371ba3a3
a, b = map(int, input().split())
if a < b:
    print("<")
elif a == b:
    print("=")
else:
    print(">")