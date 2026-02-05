# https://www.nowcoder.com/practice/c4ae7bcac7f9491b8be82ee516a94899
seconds = int(input())
h = seconds // 3600
m = seconds % 3600 // 60
s = seconds % 3600 % 60
print(h, m, s)
