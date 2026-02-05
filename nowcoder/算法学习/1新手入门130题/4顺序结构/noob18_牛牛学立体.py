# https://www.nowcoder.com/practice/3d0bd5e060154211bddc1ee892714df0
a, b, c = map(int, input().split())
S = 2 * (a * b + b * c + c * a)
V = a * b * c
print(S, V, sep="\n")
