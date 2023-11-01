class Solution {
public:
    int nthUglyNumber(int n) {
        vector<int> ugly(n);
        ugly[0]=1;
        int pt2=0,pt3=0,pt5=0;
        for(int i=1; i<n; i++){
            int next2 = ugly[pt2]*2;
            int next3 = ugly[pt3]*3;
            int next5 = ugly[pt5]*5;
            int nexug = min(next2,min(next3,next5));
            ugly[i] = nexug;
            if(ugly[i]==next2){
                pt2++;
            }
            if(ugly[i]==next3){
                pt3++;
            }
            if(ugly[i]==next5){
                pt5++;
            }
            
            
        }
        return ugly[n-1];
    }
};