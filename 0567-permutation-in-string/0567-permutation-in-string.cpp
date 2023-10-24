class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int n=s1.length(), k=s2.length();
        if(n>k) return false;
        vector<int> map1(26,0);
        vector<int> map2(26,0);
        
        for(int i=0; i<n; i++) {
            map1[s1[i]-'a']++;
            map2[s2[i]-'a']++;
        }
        
        if(map1==map2){
              return true;
        }
        
        for(int i=n; i<k; i++){
          map2[s2[i-n]-'a']--;
          map2[s2[i]-'a']++;
          if(map1==map2){
              return true;
          }
      }
        return false;
    }
};