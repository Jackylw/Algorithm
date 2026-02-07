# https://www.nowcoder.com/practice/3fed228444e740c8be66232ce8b87c2f
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPail(self, head: ListNode) -> bool:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res == res[::-1]