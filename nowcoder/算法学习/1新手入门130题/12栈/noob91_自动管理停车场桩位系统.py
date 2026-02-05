# https://www.nowcoder.com/practice/4c7f2556e7e8436189202942b4fa07e4
class Solution:
    def __init__(self):
        self.stack = []

    def push(self, node):
        return self.stack.append(node)

    def pop(self):
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def min(self):
        return min(self.stack)
