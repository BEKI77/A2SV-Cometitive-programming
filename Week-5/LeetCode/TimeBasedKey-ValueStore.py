class TimeMap:

    def __init__(self):
        self.mp = defaultdict(list)
        self.mp2 = defaultdict(list)
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].append(value)
        self.mp2[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        ind = bisect_left(self.mp2[key], timestamp)
        n = len(self.mp2[key])
        if n>0:
            if 0<ind<n and self.mp2[key][ind]!=timestamp:
                return self.mp[key][ind-1]
            elif ind == n:
                return self.mp[key][-1]
            elif ind == 0 and self.mp2[key][ind]!=timestamp:
                return ""
            else:
                return self.mp[key][ind]
        else:
            return ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)