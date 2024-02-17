# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        li = [None]*k
        cnt = 0
        cur = head
        while cur:
            cur = cur.next
            cnt+=1

        n , nk = cnt//k, cnt%k
        temp = head

        for i in range(nk):
            new = ListNode(0)
            curr = new
            j = 0
            while j<n+1:
                if temp:
                    curr.next = ListNode(temp.val)
                    curr = curr.next
                    temp = temp.next
                else:
                    curr = ListNode()
                j+=1
            li[i]=new.next

        for i in range(nk,k):
            new = ListNode(0)
            curr = new
            j = 0
            while j<n:
                if temp:
                    curr.next = ListNode(temp.val)
                    curr = curr.next
                    temp = temp.next
                else:
                    curr = ListNode()
                j+=1

            li[i]=new.next

        return li
                
                
