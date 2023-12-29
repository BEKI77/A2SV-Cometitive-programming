class Solution {
public:
    int numTimesAllBlue(vector<int>& flips) {
        int sumI=0, sumF=0,ans=0;
        for (int i=1; i<flips.size()+1; i++){
            sumI+=i;
            sumF+=flips[i-1];
            if (sumF==sumI) ans++;
        }
        return ans;
    }
};