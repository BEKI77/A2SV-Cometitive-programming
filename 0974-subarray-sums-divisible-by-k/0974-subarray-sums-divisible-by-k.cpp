class Solution {
public:
    int subarraysDivByK(vector<int>& nums, int k) {
        int sum=0, ans=0;
        // I have created a mod array count for each nums
        vector<int> modArray(k);
        modArray[0]=1;
        
        for(auto num: nums){
            sum+= (num % k + k)%k;
            ans+=modArray[sum%k];
            modArray[sum%k]++;
        }
        return ans;
    }
};