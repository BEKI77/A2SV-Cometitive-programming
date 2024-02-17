class Node:
    def __init__(self, homepage):
        self.url = homepage
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.root = Node(homepage)

    def visit(self, url: str) -> None:
        temp = self.root
        self.root.next = Node(url)
        self.root = self.root.next
        self.root.prev = temp

    def back(self, steps: int) -> str:
        i=0
        while self.root.prev and i<steps:
            self.root = self.root.prev
            i+=1
        return self.root.url
    def forward(self, steps: int) -> str:
        i = 0
        while self.root.next and i<steps:
            self.root = self.root.next
            i+=1
        return self.root.url

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)