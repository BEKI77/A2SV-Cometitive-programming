# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lessX = ListNode(0)
        moreX = ListNode(0)
        le,mo = lessX, moreX
        while head:
            if head.val<x:
                le.next = ListNode(head.val)
                le = le.next
                head = head.next
            else:
                mo.next = ListNode(head.val)
                mo = mo.next
                head = head.next
        le.next = moreX.next
        return lessX.next