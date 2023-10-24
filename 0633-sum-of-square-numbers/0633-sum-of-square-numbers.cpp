class Solution {
public:
    bool judgeSquareSum(int c) {
        for(int a=0; a<=sqrt(c); a++){
            long long squarB = c-a*a;
            long long b= sqrt(squarB);
            if(b*b==squarB) return true;
        }
        return false;
    }
};