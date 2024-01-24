class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class MyLinkedList:
    def __str__(self):
        curr = self.head
        ans = []
        while curr:
            ans.append(curr.val)
            curr = curr.next
        return str(ans)

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
            cnt = 0
            temp = self.head
            while cnt<index and temp:
                temp = temp.next
                cnt+=1
            if cnt==index and temp:
                return temp.val
            else:
                return -1

    def addAtHead(self, val: int) -> None:
        if not self.head:
            new = Node(val)
            self.head = new
        else:
            new = Node(val)
            new.next= self.head
            self.head = new


    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(val)       

    def addAtIndex(self, index: int, val: int) -> None:
        temp = self.head
        cur=0
        if not index:
            self.addAtHead(val)
        else:
            while cur<index-1 and temp:
                temp = temp.next
                cur+=1
            if cur==index-1:
                if not temp:
                    temp = Node(val)
                else:
                    new = Node(val)
                    back = temp.next
                    temp.next = new
                    new.next = back

    def deleteAtIndex(self, index: int) -> None:
        temp = self.head
        cur = 0
        if index==0:
            self.head = self.head.next if self.head.next else None  
        while cur<index-1 and temp.next:
            temp = temp.next
            cur+=1
        if cur==index-1 and temp.next:
            new = temp.next
            temp.next = new.next 
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)