class Solution {
public:
    int totalFruit(vector<int>& fr) {
        unordered_map<int,int> hash;
        int ans=0, l=0, cur=0;
        for(int r=0; r<fr.size(); r++){
            hash[fr[r]]++;
            cur++;
            while(hash.size()>2){
                int pop = fr[l];
                hash[pop]--;
                cur--;
                // the hash[pop]==0 then we need to remove it from the hash to make it valid!!
                if(!hash[pop]) hash.erase(pop);
                l++;
            }
            ans = max(ans, cur);    
        }
    return ans;
    }
};