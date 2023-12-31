class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(list(i for i in points), key=lambda x:((x[0]*x[0])+(x[1]*x[1]))**1/2)[:k]