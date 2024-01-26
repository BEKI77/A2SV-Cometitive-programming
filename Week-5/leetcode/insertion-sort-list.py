# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        ans = ListNode(0)
        ansH = ans
        while cur:
            temp = ans
            while  temp.next and temp.next.val<=cur.val:
                temp = temp.next
            next = cur.next
            cur.next = temp.next
            temp.next = cur

            cur = next
        return ans.next
