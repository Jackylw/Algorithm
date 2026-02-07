# https://www.nowcoder.com/practice/a407f7e495084084b1e1f628dfd769fd
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def vectorToListnode(self, arr: List[int]) -> ListNode:
        cur = ListNode(0)
        head = cur
        for v in arr:
            cur.next = ListNode(v)
            cur = cur.next
        return head.next
