class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        cnt = 0
        while tickets[k]:
            for i in range(len(tickets)):
                if tickets[i]:
                    tickets[i]-=1
                    cnt+=1
                    if i==k and tickets[i]==0:
                        break
        return cnt