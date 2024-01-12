class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        chk = defaultdict(int)
        l=0
        ans,cur=0,0
        for i in range(len(fruits)):
            chk[fruits[i]]+=1
            cur+=1
            while(len(chk)>2): 
                chk[fruits[l]]-=1
                cur-=1
                if not chk[fruits[l]]:
                    del chk[fruits[l]]
                l+=1
            ans = max(ans,cur)

        return ans