class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans=[]
        fL,sL=0,0
        s,e=0,0
        while fL<len(firstList) and sL<len(secondList):
            #case one if max(firstList[fl][0],secondList[sL][0])<firstList[fl][1]
            if firstList[fL][1]>secondList[sL][1]:
                s = max(firstList[fL][0],secondList[sL][0])
                e = secondList[sL][1]
                sL+=1
            elif firstList[fL][1]<secondList[sL][1]:
                s = max(firstList[fL][0],secondList[sL][0])
                e = firstList[fL][1]
                fL+=1
            else:
                s = max(firstList[fL][0],secondList[sL][0])
                e = firstList[fL][1]
                sL+=1
                fL+=1
            if s<=e:
                ans.append([s,e])
        return ans