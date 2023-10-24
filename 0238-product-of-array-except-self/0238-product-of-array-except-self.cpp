class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> answer(n);
        vector<int> leftPro(n);
        leftPro[0]=1;
        vector<int> rightPro(n);
        rightPro[n-1]=1;
        
        for(int i=1; i<n; i++){
            leftPro[i]=leftPro[i-1]*nums[i-1];
            rightPro[n-i-1]=rightPro[n-i]*nums[n-i];
        }
        
        for(int i=0; i<n;i++){
            answer[i]=leftPro[i]*rightPro[i];
        }
        
        return answer;
    }
};