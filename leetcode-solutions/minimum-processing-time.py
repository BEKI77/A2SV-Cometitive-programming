class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        return max(time + task for (time,task) in zip(sorted(processorTime), sorted(tasks)[::-4]))
       
       
       
       
        # n = len(processorTime)
        # processorTime.sort()
        # tasks.sort()
        # ans=0
        # j=3
        # print(tasks)
        # for i in range(n-1,-1,-1):
        #     ans = max(ans, processorTime[i] + tasks[j])
        #     j+=4
        # return ans