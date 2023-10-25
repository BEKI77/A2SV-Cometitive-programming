class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int ans=0, no_zeros=0,l=0;
        for(int i=0; i<nums.size(); i++){
            if(nums[i]==0) no_zeros++;
            while(no_zeros>k){
                if(nums[l]==0) no_zeros--;
                l++;
            }
            ans = max(ans,i-l+1);
        }
        
        return ans;
    }
};