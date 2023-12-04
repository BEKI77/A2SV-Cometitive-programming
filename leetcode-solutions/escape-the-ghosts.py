class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        moves = abs(target[0])+abs(target[1])
        for i in ghosts:
            gmovX=abs(target[0]-i[0])
            gmovY=abs(target[1]-i[1])
            gmv=gmovX+gmovY
            print(gmv)
            if gmv<=moves:
                return False
        return True