class Solution {
public:
    int missingNumber(vector<int>& nums) {
        /*
        sort(nums.begin(),nums.end());
        for(int i=0; i<nums.size(); i++) {
            if(nums[i]!=i) return i;
        }
        return nums.size();
        */
        int sum=nums.size(), act=0;
        for(int i=0; i<nums.size(); i++){
            sum+=i;
            act+=nums[i];
        }
        return sum-act;
    }
};