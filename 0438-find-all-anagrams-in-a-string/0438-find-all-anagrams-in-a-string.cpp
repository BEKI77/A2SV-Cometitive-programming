class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        int n = p.length();
        vector<int> ans;
        if(n>s.length()) return ans;
        vector<int> chk(26,0);
        vector<int> hash(26,0);
        for(int i=0; i<n; i++){
            hash[s[i]-'a']++;
            chk[p[i]-'a']++;
        }
        if(chk==hash) ans.push_back(0);
        for(int i=n; i<s.length(); i++) {
            hash[s[i-n]-'a']--;
            hash[s[i]-'a']++;
            if(chk==hash) ans.push_back(i-n+1);
        }
        
        return ans;
    }
};