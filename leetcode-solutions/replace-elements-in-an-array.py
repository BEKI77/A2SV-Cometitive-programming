class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        map = dict()
        for i, val in enumerate(nums):
            map[val]= map.get(val,i)
        for op in operations:
           nums[map[op[0]]]=op[1]
           map[op[1]]=map[op[0]]
        return nums

    