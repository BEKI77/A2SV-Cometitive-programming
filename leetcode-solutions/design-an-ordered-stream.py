class OrderedStream:
    lptr,ptr=0,0
    def __init__(self, n: int):
        self.arr=[0]*n

    def insert(self, idKey: int, value: str) -> List[str]:
        self.arr[idKey-1]=value
        if self.ptr==idKey-1:
            while self.ptr<len(self.arr) and self.arr[self.ptr]!=0:
                self.ptr+=1
        curr=[ self.arr[i] for i in range(self.lptr,self.ptr)]
        self.lptr=self.ptr
        return curr


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)