class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        ans=inf
        dic = defaultdict(int)
        for i in range(len(cards)):
            if cards[i] in dic:
               ans=min(ans,i-dic[cards[i]]+1)

            dic[cards[i]]=i 

        if ans==inf:
            return -1
        else:
            return ans
