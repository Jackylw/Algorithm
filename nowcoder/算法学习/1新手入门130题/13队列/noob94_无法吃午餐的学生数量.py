# https://www.nowcoder.com/practice/2dac3d7567f741a88ec551caf907934d
from collections import deque
from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stu = deque(students)
        sandwich = deque(sandwiches)
        n_stu = 0 # 不匹配的学生数
        while n_stu < len(stu):
            if stu[0] == sandwich[0]:
                stu.popleft()
                sandwich.popleft()
                n_stu = 0
            else:
                stu.append(stu.popleft())
                n_stu += 1
        return len(stu)
