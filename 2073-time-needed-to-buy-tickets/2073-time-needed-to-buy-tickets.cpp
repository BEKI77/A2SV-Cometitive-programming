class Solution {
public:
    int timeRequiredToBuy(vector<int>& tickets, int k) {
        int cnt=0;
        while(tickets[k]){
            for(int i=0; i<tickets.size(); i++){
               if(tickets[i]){
                    tickets[i]--;
                    cnt++;
                    if(i==k && tickets[i]==0) break;
                }
            }
        }
        return cnt;
    }
};