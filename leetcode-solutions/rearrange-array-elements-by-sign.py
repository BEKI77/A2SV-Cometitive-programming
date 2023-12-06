class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p=[]
        n=[]
        ans=[]
        for i in range(len(nums)):
            if nums[i]>0:
                p.append(nums[i])
            else:
                n.append(nums[i])
        for i in range(len(nums)//2):
            ans.append(p[i])
            ans.append(n[i])
        return ans

                