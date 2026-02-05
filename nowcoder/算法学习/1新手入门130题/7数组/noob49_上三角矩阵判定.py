# https://www.nowcoder.com/practice/f5a29bacfc514e5a935723857e1245e4
n = int(input())
nums = []
for _ in range(n):
    nums.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(0, i):
        if nums[i][j] != 0:
            print("NO")
            exit()
print("YES")

