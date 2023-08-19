class Solution {
public:
    vector<int> pancakeSort(vector<int>& arr) {
        vector<int> ans;
        if(is_sorted(arr.begin(), arr.end())) return ans;
        int start = 0, end = arr.size() - 1;
        while(start < end){
            int maxIdx = 0;
            int maxVal = 0;
            for(int i = start; i <= end; i++){
                if(arr[i] > maxVal){
                    maxIdx = i;
                    maxVal = arr[i];
                }
            }
            int lo = start, hi = maxIdx;
            ans.push_back(maxIdx + 1);
            while(lo < hi) swap(arr[lo++], arr[hi--]);
            
            lo = start, hi = end;
            while(lo < hi) swap(arr[lo++], arr[hi--]);
            ans.push_back(end + 1);
            --end;
        }
        
        for(int i=0; i<arr.size(); i++) cout<<arr[i];
        return ans;
    }
};
