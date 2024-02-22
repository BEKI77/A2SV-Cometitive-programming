class MyCircularQueue:

    def __init__(self, k: int):
        self.li = []
        self.size = k

    def enQueue(self, value: int) -> bool:
        if len(self.li)== self.size:
            return False
        else:
            self.li.append(value)
            return True

    def deQueue(self) -> bool:
        if self.li:
            self.li.pop(0)
            return True
        else:
            return False

    def Front(self) -> int:
        return self.li[0] if self.li else -1 

    def Rear(self) -> int:
        return self.li[-1] if self.li else -1

    def isEmpty(self) -> bool:
        return not self.li

    def isFull(self) -> bool:
        return len(self.li)==self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()