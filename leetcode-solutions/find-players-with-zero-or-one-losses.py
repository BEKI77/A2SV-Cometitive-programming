class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losers= {}
        winners=set()
        for i in matches:
            winners.add(i[0])
            losers[i[1]]=losers.get(i[1],0)+1
        answ=set()
        ansl=set()
        for i in matches:
            if i[0] not in losers:
                answ.add(i[0])

        for l,val in losers.items():
            if val==1:
                ansl.add(l)

        return [sorted(answ),sorted(ansl)]