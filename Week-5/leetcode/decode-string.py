class Solution:
    def decodeString(self, s: str) -> str:
        def decode(s,p):
            res = ""
            i,num = p,''
            while i<len(s):
                if s[i].isdigit():           
                    num+=s[i]
                elif s[i]=="[":
                    local,pos = decode(s,i+1)
                    res+=local*int(num)
                    i=pos
                    num=''
                elif s[i]=="]":
                    return res,i
                else:
                    res+=s[i]
                i+=1
            return res,i
    
        return decode(s,0)[0]
	
       