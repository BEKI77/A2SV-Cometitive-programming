class Solution {
public:
    string addSpaces(string s, vector<int>& spaces) {
        vector<string> arr;
        int cnt=0, n = spaces.size();
        string ans, res="";    
        for(int i=0; i<n; i++){
            ans = s.substr(cnt,spaces[i]-cnt);
            cnt=spaces[i];
            arr.push_back(ans);    
        }
            ans=s.substr(spaces[n-1], s.size()-spaces[n-1]);
            arr.push_back(ans);
        for(int i=0; i<arr.size(); i++){
            res+=arr[i]+" ";
        }
        res.pop_back();
        return res;
    }
};
