# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oddNod = ListNode(0)
        evenNod = ListNode(0)
        eve,odd = evenNod, oddNod
        cur = 1
        while head:
            if cur%2:
                odd.next= ListNode(head.val)
                odd = odd.next
                head = head.next
            else:
                eve.next = ListNode(head.val)
                eve = eve.next
                head = head.next
            cur+=1
        odd.next = evenNod.next
        return oddNod.next