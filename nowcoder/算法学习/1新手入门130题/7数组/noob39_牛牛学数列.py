# https://www.nowcoder.com/practice/b6321648517247b2ac2e2f80cbc63ae1
n = int(input()) - 1
An = [0, 1, 1]
if n < 3:
    print(An[n])
    exit()
for i in range(3, n + 1):
    An.append(An[i - 1] + 2 * An[i - 2] + An[i - 3])
print(An[n])
