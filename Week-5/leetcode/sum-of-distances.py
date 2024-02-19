class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        dic = defaultdict(list)
        totcnt = defaultdict(int)
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]].append(0)
                dic[nums[i]].append(i)
            else:
                temp = dic[nums[i]][-1]
                dic[nums[i]].append(temp+i)

            totcnt[nums[i]]+=1

        ans = [0]*len(nums)
        cnt = defaultdict(int)

        for i in range(len(nums)):
            prev =  cnt[nums[i]]
            prevSum = dic[nums[i]][cnt[nums[i]]]
            suff = totcnt[nums[i]]-cnt[nums[i]]
            suffSum = dic[nums[i]][-1]-dic[nums[i]][cnt[nums[i]]]
            ans[i] = abs(prevSum - prev*i + i*suff - suffSum)
            print(prev, prevSum, suff, suffSum) 
            cnt[nums[i]]+=1
      
        return ans