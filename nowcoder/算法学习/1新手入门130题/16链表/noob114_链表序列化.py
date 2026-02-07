# https://www.nowcoder.com/practice/9e36b4349f0441d8a2c31ceeb46c757e
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def listnodeToVector(self, head: ListNode) -> List[int]:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res
