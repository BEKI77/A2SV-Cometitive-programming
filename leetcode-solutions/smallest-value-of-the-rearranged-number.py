class Solution:
    def smallestNumber(self, num: int) -> int:
        nums = list(str(num))
        holder = set()
        ans=0
        if num>=0:
            arr=[]
            for i in nums:
                if i!='0':arr.append(i)
            arr.sort()
            if len(arr)>0:
                temp=arr[0]
                Noz=len(nums)-len(arr)
                while Noz>0: 
                    temp+='0'
                    Noz-=1
                temp+=''.join(arr[1:])
                ans = int(temp)
            else:ans = 0
        else:
            nums = nums[1:]
            for i in range(0,len(nums)):
                for j in range(0,len(nums)-1):
                    holder.add(''.join(nums))
                    if nums[j]+nums[j+1]<=nums[j+1]+nums[j]:
                        nums[j],nums[j+1]=nums[j+1],nums[j]
            temp = sorted(list(holder))
            i=0
            while i+1<len(temp) and temp[i][0]=='0': i+=1 
            ans = int('-'+temp[-1])
        return ans