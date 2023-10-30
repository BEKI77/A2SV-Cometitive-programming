class Solution {
public:
    string shiftingLetters(string s, vector<vector<int>>& shifts) {
        string ans;
        vector<int> cnt(s.length()+1,0);
        for(int i=0; i<shifts.size(); i++){
            if(shifts[i][2]){
                cnt[shifts[i][0]]++;
                cnt[shifts[i][1]+1]--;
            }else{
                cnt[shifts[i][0]]--;
                cnt[shifts[i][1]+1]++;
            }
        }
        
        for(int i=1; i<cnt.size(); i++) cnt[i]= cnt[i]+cnt[i-1];
        
        for(int i=0; i<s.length(); i++) {
            int a=s[i]-'a';
            if(a+cnt[i]>=0){
                ans.push_back('a'+((a+cnt[i])%26));
            }else{
                if((a+cnt[i])%26==0){
                    ans.push_back('a'+((a+cnt[i])%26));
                }
                else{ans.push_back('a'+((a+cnt[i])%26)+26);}
            } 
        };
        return ans;
    }
};