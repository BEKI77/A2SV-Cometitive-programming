class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l,r= 0, len(letters)-1
        ans = l
        while l<=r:
            m = l+((r-l)//2)  
            if letters[m]>target:
                ans= m
                r = m-1
            else:
                l = m+1

        return letters[ans]