class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        int ope=0, i=0,j=nums.size()-1;
        sort(nums.begin(),nums.end());
     while(i < j)
   {
   	  int sum = nums[i] + nums[j];
   	  if(sum == k)
   	  {
   	     ope++;
		 i++;
		 j--;	
      }
      else if(sum < k)
      {
      	  i++;
	  }
	  else if(sum > k)
	  {
	  	 j--;
	  }
   }
    return ope;
    }
};
 