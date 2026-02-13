# https://ac.nowcoder.com/acm/contest/120565/J
import sys

input = sys.stdin.readline


# 判断矩阵的行\列\对角线是否满足条件
def check_matrix(matrix):
    check_num = sum(num for num in matrix[0])
    for row in matrix:
        if sum(num for num in row) != check_num:
            return False
    for row in range(3):
        if sum(matrix[row][i] for i in range(3)) != check_num:
            return False
    if sum(matrix[i][i] for i in range(3)) != check_num:
        return False
    set_nums = set()
    for row in matrix:
        for num in row:
            set_nums.add(num)
    if len(set_nums) != 9:
        return False
    return True


def f():
    matrix = []
    for _ in range(3):
        row = list(map(int, input().split()))
        matrix.append(row)
    check = check_matrix(matrix)
    if check:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    f()
