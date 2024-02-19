class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cnt5 = 0
        cnt10 = 0
        for i in bills:
            if i==5:
                cnt5+=i
            elif i==10:
                cnt5-=5
                cnt10+=10
                if cnt5<0:
                    return False
            elif i==20:
                chk1,chk2 = False,False
                if not (cnt5-5<0  or cnt10-10<0):
                    cnt5-=5
                    cnt10-=10
                    chk1=True
                elif not (cnt5-15<0):
                    cnt5-=15
                    chk2 = True
                
                if chk1 == False and chk1==chk2:
                    return False
        return True