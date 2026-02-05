# https://www.nowcoder.com/practice/0b5afb815f6848d9a7f9c1b0ce514b95
s1, s2 = map(str, input().split())
rules = {
    "elephant": "tiger",
    "tiger": "cat",
    "cat": "mouse",
    "mouse": "elephant"
}

if rules[s1] == s2:
    print("win")
elif rules[s2] == s1:
    print("lose")
else:
    print("tie")