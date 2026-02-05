# https://www.nowcoder.com/practice/54275ddae22f475981afa2244dd448c6
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        self.stack1.append(node)

    def pop(self):
        ans = self.stack1.pop(0)
        return ans
