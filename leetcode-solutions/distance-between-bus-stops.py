class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        tot = sum(distance)
        ans=0
        if start<destination:
            ans=min(sum(distance[start:destination]), tot-sum(distance[start:destination]))
        else:
            mid = (tot-sum(distance[0:start])) + sum(distance[0:destination])
            ans = min(mid,tot-mid)
        return ans