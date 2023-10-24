class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int n= nums.size(), ans=0;
        vector<int> prefixSum(n);
        
        prefixSum[0]=nums[0];
        
        for(int i=1; i<n; i++)
            prefixSum[i]=prefixSum[i-1]+nums[i];
       
        unordered_map<int,int> countOfPrefix;

        for(int i=0; i<n; i++){
       
            if(prefixSum[i]==k)
                ans++;
            
            if(countOfPrefix.find(prefixSum[i]-k)!=countOfPrefix.end()){
                ans+=countOfPrefix[prefixSum[i]-k];
            }
            
            countOfPrefix[prefixSum[i]]++;
        }
      return ans;  
    }
};