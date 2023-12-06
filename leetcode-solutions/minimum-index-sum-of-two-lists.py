class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        arr = {}
        mi =float('inf')
        ans=[]
        for i in range(len(list1)):
            if list1[i] in list2:
                arr[list1[i]]= i+list2.index(list1[i])
                mi= min(mi,i+list2.index(list1[i]))
        for i,val in arr.items():
            if val==mi:
                ans.append(i)
       
        return ans