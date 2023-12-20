class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry=1
        for i in range(len(digits)-1,-1,-1):
            if digits[i]+carry > 9:
                digits[i]=0
                carry=1
            elif digits[i]+carry<=9:
                digits[i]+=carry
                carry=0
                break
            else: 
                carry=0
        if carry:
            digits.insert(0,1)
        return digits