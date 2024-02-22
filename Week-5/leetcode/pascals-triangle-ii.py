class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def fact(i)->int:
            return 1 if i==0 else i*fact(i-1)
        ans = [0]*(rowIndex+1)
        for i in range(rowIndex+1):
            ans[i] = (fact(rowIndex)//(fact(i)*fact(rowIndex-i)))
        return ans