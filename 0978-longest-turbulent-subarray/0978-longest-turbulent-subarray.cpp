class Solution {
public:
    int maxTurbulenceSize(vector<int>& arr) {
        int cnt=1, n=arr.size(),r=0;
        auto comp = [&](int x, int y){
            if(x<y) return -1;
            else if(x>y) return 1;
            else return 0;
        };
        for(int i=1; i<n; i++){
            int c = comp(arr[i-1],arr[i]);
            if(c==0) r=i;
            else if(i==n-1 || c*comp(arr[i],arr[i+1])!=-1){
                cnt = max(cnt,i-r+1);
                r=i;
            }
            
        }
        return cnt;
    }
};