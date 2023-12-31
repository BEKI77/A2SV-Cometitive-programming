class Solution {
public:
    int maxIceCream(vector<int>& costs, int coins) {
        int  ans = 0;
        int mx = 0;
        for (int i:costs) mx = (i>mx? i:mx);
        vector<int> sorted(mx+1,0);
        for(int i=0; i<costs.size(); i++){
            sorted[costs[i]]+=1;
        }
        for(int i=0; i<mx+1; i++){
            if(sorted[i]!=0 && coins>0){
                while(sorted[i]>0 && coins>0){
                    if (coins-i>=0){
                        coins-=i;
                        sorted[i]-=1;
                        ans++;
                    }else{
                        break;
                    }
                }
            }
        }
        return ans;
    }
};