class Solution {
public:
    bool isAnagram(string s, string t) {
        
        if(s.length()!=t.length()) return false;
        else{
            int n = s.length();
            vector<int> hash1(26,0),hash2(26,0);
            for(int i=0; i<s.length(); i++){
                hash1[s[i]-'a']++;
                hash2[t[i]-'a']++;
            }
            if(hash1!=hash2) return false;
        }
            
        return true;
    }
};