class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        double n = nums.size(),
            maxM,
            curM;
        for(int i=0; i<k; i++) curM+=nums[i];
        maxM = curM;
        for(int i=k; i<n; i++){
            curM = curM-nums[i-k]+nums[i];
            maxM = max(maxM, curM);  
        }
        return maxM/k;
    }
};