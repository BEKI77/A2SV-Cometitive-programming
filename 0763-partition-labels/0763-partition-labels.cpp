class Solution {
public:
    vector<int> partitionLabels(string s) {
        vector<int> ans;
        int l=0;
        unordered_map<char,int> last;
        for(int i=0; i<s.length(); i++){
            last[s[i]]=i;
        }
        int r=last[s[0]];
        for(int i=0; i<s.length(); i++){
            if(last[s[i]]>r) r=last[s[i]];
            
            if(i==r) {
                ans.push_back(i-l+1);
                l=i+1;
            }
        }
        return ans;
    }
};