# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        li1 = set()
        li2 = set()
        while headA and headB:
            li1.add(headA)
            li2.add(headB)
            if headA in li2:
                return headA
            elif headB in li1:
                return headB
            headA = headA.next
            headB = headB.next
        if headB:
            while headB:
                if headB in li1:
                    return headB
                headB = headB.next
        elif headA:
            while headA:
                if headA in li2:
                    return headA
                headA = headA.next
