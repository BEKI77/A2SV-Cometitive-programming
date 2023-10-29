class DataStream {
    int val,n;
    int cnt=0;
    queue<int> arr;
public:
    DataStream(int value, int k) {
        val=value;
        n=k;
    }
    
    bool consec(int num) {
        arr.push(num);
        if(num==val){
            cnt++;
        }else{
            cnt=0;
        }
        
        return cnt>=n;
    }
};

/**
 * Your DataStream object will be instantiated and called as such:
 * DataStream* obj = new DataStream(value, k);
 * bool param_1 = obj->consec(num);
 */