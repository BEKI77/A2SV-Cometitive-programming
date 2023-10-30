class Solution {
public:
    int maxProfit(vector<int>& pr) {
        int l=0,r=1;
        int prof=0;
        if(pr.size()==1) return 0;
        
        while(r<pr.size()){
            if(pr[l]>pr[r]){
                l=r;
            }else{
                prof= max(prof,pr[r]-pr[l]);
            }
            r++;
        }
        
        return prof;
    }
};