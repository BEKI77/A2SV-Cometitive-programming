class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int cnt=0;
        for(int i=0; i<nums.size(); i++){
            if(nums[i]==val) nums[i]=INT_MAX;
            else cnt++;  
        }
        sort(nums.begin(),nums.end());
        return cnt;
    }
};