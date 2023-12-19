class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        cnt=0
        table = defaultdict(list)
        for i in range(len(nums)):
            if nums[i] in table:
                for j in table[nums[i]]:
                    if (j*i)%k==0:
                        cnt+=1
            table[nums[i]].append(i)
        return cnt