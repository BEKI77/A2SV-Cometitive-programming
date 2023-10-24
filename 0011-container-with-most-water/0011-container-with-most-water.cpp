class Solution {
public:
    int maxArea(vector<int>& height) {
        int maxA=0, r = height.size()-1, l=0;
        while(l<r){
            int wi = r-l;
            
            int hi = min(height[l],height[r]);
            
            maxA = max(maxA, hi*wi);
            if(height[l]>height[r]){
                r--;
            }else{
                l++;
            }
        }
        return maxA;
    }
};