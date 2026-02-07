# https://www.nowcoder.com/practice/d8b6b4358f774294a89de2a6ac4d9337
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def Merge(self, pHead1: ListNode, pHead2: ListNode) -> ListNode:
        dummy = ListNode(0)
        head = dummy
        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                head.next = pHead1
                pHead1 = pHead1.next
            else:
                head.next = pHead2
                pHead2 = pHead2.next
            head = head.next
        if pHead1:
            head.next = pHead1
        if pHead2:
            head.next = pHead2
        return dummy.next
