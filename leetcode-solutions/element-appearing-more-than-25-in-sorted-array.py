class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        map={}
        for i in arr:
            map[i]= map.get(i,0)+1
        for i,val in map.items():
            if val>len(arr)*0.25:
                return i
        else:
            return 0