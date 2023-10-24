class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int maxL=0, r=0,l=0;
        unordered_map<char,int> mp;
        
        while(r<s.length()){
            mp[s[r]]++;
            if(mp.size()==r-l+1){
                maxL = max(maxL,r-l+1);
            }else if(mp.size()<r-l+1){
                while(mp.size()<r-l+1){
                    mp[s[l]]--;
                    if(mp[s[l]]==0) mp.erase(s[l]);
                    l++;
                }
            }
            r++;
        }
        
        return maxL;
    }
};