class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        set<vector<int>> ans;
        sort(nums.begin(), nums.end());
        vector<vector<int>> sol;
        for(int i=0; i<nums.size(); i++){
            int j=i+1, k=nums.size()-1;
            while(j<k){
                int sum = nums[i] + nums[j] + nums[k];
                if(sum==0){
                    ans.insert({nums[i],nums[j],nums[k]});
                    j++;
                    k--;
                }else if(sum>0){
                    k--;
                }else{
                    j++;
                }
            }
        }
        
        for(auto i: ans){
            sol.push_back(i);
        }
    
        return sol;
        
    }
};