class Solution {
public:
    string largestMerge(string w1, string w2) {
        int n = w1.length(), m = w2.length();
        string ans="";
        int l=0,r=0;
        while(l < n && r < m){
            if(w1[l] > w2[r]) {
                ans+=w1[l];
                l++;
            }else if(w1[l]< w2[r]){
                ans+=w2[r];
                r++;
            }else{
                if(w1.substr(l+1) > w2.substr(r+1)){
                    ans+=w1[l];
                    l++;
                }else{
                    ans+=w2[r];
                    r++;
                }
            }
        }
        
        while(l<n) ans+=w1[l++];
        while(r<m) ans+=w2[r++];
 
        return ans;
    }
};