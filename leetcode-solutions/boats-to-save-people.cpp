class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit){
        int r = people.size()-1,l=0, numB=0 ;
        sort(people.begin(),people.end());
       
        while(l<=r){
            if(people[l]+people[r]<=limit){
                l++;
                r--;
            }else r--;
            numB++;
        }
        return numB;
    }
};