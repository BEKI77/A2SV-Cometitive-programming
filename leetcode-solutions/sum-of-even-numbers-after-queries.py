class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans=[]
        esum = sum(i for i in nums if i%2==0)
        for i in queries:
            temp=nums[i[1]]
            if temp%2 != 0 and (temp+i[0])% 2 == 0:
                nums[i[1]]+=i[0]
                esum +=(temp+i[0])
                ans.append(esum)
            elif temp%2== 0 and (temp+i[0])%2==0:
                nums[i[1]]+=i[0]
                esum+=i[0]
                ans.append(esum)
            elif temp%2 == 0 and (temp+i[0])%2!=0:
                nums[i[1]]+=i[0]
                esum-=temp
                ans.append(esum)
            else:
                nums[i[1]]+=i[0]
                ans.append(esum)

            
        return ans