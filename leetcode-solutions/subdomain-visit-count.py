class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        Dic = dict()
        for dom in cpdomains:
            cnt, www = dom.split()
            Edom = list(www.split('.'))
            for i in range(len(Edom)):
                Dic['.'.join(Edom[i:])]=Dic.get('.'.join(Edom[i:]),0)+int(cnt)
    
        return [f'{val} {i}' for i,val in Dic.items()]
       