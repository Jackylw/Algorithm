# https://www.nowcoder.com/practice/428a854dff8b4333b54cfe580323e2df
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self , head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return dummy.next