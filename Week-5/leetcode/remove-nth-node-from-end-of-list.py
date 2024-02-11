# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        cnt = 0
        while curr:
            curr= curr.next
            cnt+=1
        new = head
        i = 0
        if cnt-n==0:
            return head.next
        else:
            while new and i<(cnt-n)-1:
                new = new.next
                i+=1
            if new and new.next:
                new.next = new.next.next
            else:
                return None
        return head