class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        deck.sort()
        ans =[0]*(n)
        que = []
        for i in range(n): 
            que.append(i)

        for i in deck:
            ans[que[0]] = i
            que.pop(0)
            if que:
                que.append(que[0])
                que.pop(0)
        return ans