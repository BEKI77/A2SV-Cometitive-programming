class Solution {
public:
    int maxProfit(vector<int>& pr) {
        int l=0,r=1;
        int maxP=0;
        if(pr.size()<=1) return 0;
        while(r<pr.size()){
            if(pr[l]>pr[r]){
                l++;
            }else{
                maxP+=pr[r]-pr[l];
                l++;
            }
            r++;
        }
        return maxP;
    }
};