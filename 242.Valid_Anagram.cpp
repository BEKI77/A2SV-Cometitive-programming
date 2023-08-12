class Solution {
public:
    bool isAnagram(string s, string t) {
        int cnt=0;
        if(s.size()==t.size()){
            sort(s.begin(), s.end());
            sort(t.begin(), t.end());
            for(int i=0; i<s.size(); i++){
                if(s[i]==t[i]) cnt++; 
            }
        }
        return cnt==s.size();
    }
};
