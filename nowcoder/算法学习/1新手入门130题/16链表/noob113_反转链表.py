# https://www.nowcoder.com/practice/75e878df47f24fdc9dc3e400ec6058ca
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def ReverseList(self, head: ListNode) -> ListNode:
        cur = head
        pre = None
        if head is None:
            return None
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

