class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        l1,l2=0,0
        if name[l1]!=typed[l2]:
            return False
        fl=False
        while l1<len(name) and l2<len(typed):
            while l2<len(typed) and name[l1]!=typed[l2]:
                if l1>0 and name[l1-1]!=typed[l2]:
                    return False
                l2+=1
            if l2<len(typed) and l1<len(name) and name[l1]==typed[l2]:
                l1+=1
                l2+=1
            
        if l1==len(name):
            while l2<len(typed):
                if name[l1-1]==typed[l2]:
                    l2+=1
                else:
                    return False
            return True
        else:
            return False