class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        table1=[ arr1[i] for i in range(len(arr1)) if arr1[i] not in arr2]
        table1.sort()
        dic = Counter(arr1)
        ans=[]
        for i in arr2:
            while dic[i]>0:
                ans.append(i)
                dic[i]-=1
        for i in table1:
            ans.append(i)
        return ans