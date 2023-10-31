class Solution {
public:
    bool validPalindrome(string s) {
        int l=0,r=s.length()-1;
        bool ans=true;
        bool chk = false;
        while(l<=r){
         if(s[l]==s[r]){
             l++, r--;
         }else{
             int ld=l+1, rd=r;
             bool t1=true, t2=true; 
             while(ld+1<=rd){
                 if(s[ld]==s[rd]){
                     ld++;
                     rd--;
                 }else {
                     t1=false;
                     break;
                 }
             }
             ld=l,rd=r-1;
             while(ld<=rd){
                 if(s[ld]==s[rd]){
                     ld++;
                     rd--;
                 }else {
                     t2=false;
                     break;
                 }
             }
             chk=true;
             ans=t1||t2;
         }
            if(chk) break;
        }
        
        return ans;
    }
};