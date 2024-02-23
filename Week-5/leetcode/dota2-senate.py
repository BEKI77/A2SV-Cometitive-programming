class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        liR = []
        liD = []
        n = len(senate)
        for i in range(len(senate)):
            if senate[i]=='D':
                liD.append(i)
            else:
                liR.append(i)

        while liD and liR:
            if liD[0]<liR[0]:
                liR.pop(0)
                liD.append(liD.pop(0)+n)
            else:
                liD.pop(0)
                liR.append(liR.pop(0)+n)
        
        return "Radiant" if liR else "Dire"  

            

        