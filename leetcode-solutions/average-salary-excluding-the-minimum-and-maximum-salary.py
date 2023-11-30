class Solution:
    def average(self, salary: List[int]) -> float:
        ma,mi,sum=salary[0],salary[0],0
        for i in salary:
            sum+=i
            if i<mi:
                mi=i
            if i>ma:
                ma=i


        return (sum-mi-ma)/(len(salary)-2)