class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
       unordered_map<int,int> visited; 
       int len = nums.size();
       for(int i=0; i<len; ++i){
           int n= nums[i];
           int compliment= target - n;
           if(visited.count(compliment)){
               return{visited[compliment],i};
           }
           visited[n]=i;
       }
       return{};
    }
};