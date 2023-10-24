class Solution {
public:
    int characterReplacement(string s, int k) {
        int ans=0, l=0;
        vector<int> hash(26,0);
        for(int r=0; r<s.length(); r++){
            hash[s[r]-'A']++;
            while(((r-l+1) - *max_element(hash.begin(),hash.end()))>k ){
                hash[s[l]-'A']--;
                l++;
            }
            ans = max(ans,r-l+1);
        }
        return ans;
    }
};