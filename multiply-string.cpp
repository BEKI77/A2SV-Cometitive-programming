class Solution {
public:
    string multiply(string num1, string num2) {
        if(num1[0]=='0'|| num2[0]=='0') return"0";
        int n = num1.size()+num2.size();
        string ans="";
        vector<int> arr(n,0);
        for(int i=num1.size()-1; i>=0; i--){
           for(int j=num2.size()-1; j>=0; j--){
               arr[i+j+1] += int(num1[i]-'0')*int(num2[j]-'0');
               arr[i+j] += arr[i+j+1]/10;
               arr[i+j+1] %=10;
           }
        }
        int i=0;
        while(arr[i]==0) i++;
        while(i < arr.size()) ans+=to_string(arr[i++]);
        return ans;
    }
};
