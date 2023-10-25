class Solution {
public:
    int matchPlayersAndTrainers(vector<int>& pl, vector<int>& tr) {
        int ans=0,l=0,r=0;
        sort(pl.begin(),pl.end());
        sort(tr.begin(), tr.end());
        while(l<pl.size() && r < tr.size()){
            if(pl[l]<=tr[r]){
                ans++;
                l++,r++;
            }else r++;
        }
        return ans;
    }
};