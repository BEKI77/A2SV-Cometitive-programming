class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int cnt=0;
        map<int,int> mp;
        for(int i=0; i<nums.size(); i++) mp[nums[i]]++;
        int i=0;
        for(auto j:mp){
            nums[i]=j.first;
            i++;
        }
        return i;
    }
};