class Solution {
public:
    int maxDistance(vector<int>& nums1, vector<int>& nums2) {
        int l=0,r=0,ans=0;
        while(l<nums1.size() && r<nums2.size()){
            int cur=0;
            if(nums1[l]>nums2[r]){
                l++;
            }else if(nums1[l]<=nums2[r]){
                cur=r-l;
                r++;
            }
           ans=max(ans,cur);     
        }
        return ans;
    }
};