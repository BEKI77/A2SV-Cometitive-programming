class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        map = [[names[i],heights[i]] for i in range(len(names))]
        map.sort(key = lambda x:x[1],reverse = True)
        return [map[i][0] for i in range(len(names))]