# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import copy
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        prv = None
        ohead = copy.deepcopy(head)
        cur = head
        while cur:
            new = cur.next
            cur.next = prv
            prv = cur
            cur = new
        while prv and ohead:
            if prv.val != ohead.val:
                return False
            prv = prv.next
            ohead = ohead.next
        
        return True
