class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        cnt = Counter(answers)
        ans = 0
        for i in cnt:
            ans += (math.ceil(cnt[i]/(i+1)))*(i+1)
        
        return ans