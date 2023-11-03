class Solution {
public:
    int findTheWinner(int n, int k) {
        queue<int> nums;
        for(int i=1; i<=n; i++){
            nums.push(i);
        }
        while(nums.size()>1){
                for(int i=1; i<k; i++){
                    int cur = nums.front();
                    nums.pop();
                    nums.push(cur);
                }
            nums.pop();
        }
        return nums.front();
    }
};