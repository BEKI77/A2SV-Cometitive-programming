class MyStack:

    def __init__(self):
        self.li = []

    def push(self, x: int) -> None:
        self.li.append(x)

    def pop(self) -> int:
        fl = False
        if self.li:
            fl = True
            temp = self.li[-1]
            self.li.pop()
        return temp if fl else None

    def top(self) -> int:
        return self.li[-1] if self.li else None

    def empty(self) -> bool:
        return not self.li


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()