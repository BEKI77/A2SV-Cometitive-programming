class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int n = nums.size(), ans= n+1, Rsum=0, leftPo=0;
        for(int i=0; i<n; i++){
            Rsum+=nums[i];
            while(Rsum>=target){
                ans= min(ans, i+1-leftPo);
                Rsum-=nums[leftPo++];
            }
        }
        return (ans != n+1) ? ans:0;
    }
};