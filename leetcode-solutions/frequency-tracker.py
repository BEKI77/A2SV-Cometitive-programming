class FrequencyTracker:

    def __init__(self):
        self.arr = defaultdict(int)
        self.cnt = defaultdict(int)
        

    def add(self, number: int) -> None:
        self.cnt[self.arr[number]] -= 1
        self.arr[number] += 1
        self.cnt[self.arr[number]] += 1

        

    def deleteOne(self, number: int) -> None:
        if self.arr[number] > 0:
            self.cnt[self.arr[number]] -= 1
            self.arr[number] -= 1
            self.cnt[self.arr[number]] += 1
        

    def hasFrequency(self, frequency: int) -> bool:
        return self.cnt[frequency]
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)