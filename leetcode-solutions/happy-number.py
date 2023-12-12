class Solution:
    def isHappy(self, n: int) -> bool:
        map = dict()
        if n==1 : return True
        while(n!=1):
            temp = str(n)
            n=0
            for i in range(len(temp)):
                val = int(temp[i])
                n+=val*val
            map[n]=map.get(n,0)+1
            if n==1: return True
            elif map[n]>2: return False