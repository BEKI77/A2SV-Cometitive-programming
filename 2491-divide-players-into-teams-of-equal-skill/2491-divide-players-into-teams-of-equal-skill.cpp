class Solution {
public:
    long long dividePlayers(vector<int>& skill) {
        int n = skill.size();
        sort(skill.begin(),skill.end());
        int sk=skill[0]+skill[n-1];
        long long ans=0;
        for(int i=0,j=n-1; i<n/2; i++,j--){
            if(sk!=skill[i]+skill[j]) return -1;
            ans=ans+skill[i]*skill[j];
        }
        return ans;
    }
};