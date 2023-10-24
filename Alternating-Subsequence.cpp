#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(NULL), cout.tie(NULL);
    int t;
    cin>>t;
    while(t--){
        ll n;
        auto sign = [&](int x) {
            if(x>0) return 1;
            else return -1;
        };

        cin>>n;
        vector<ll> arr(n);
        for(auto &i:arr) cin>>i;
        ll sum=0;
        for(int i=0; i<n; i++){
           int cur=arr[i]; 
           int j=i;
           while(j<n && sign(arr[i])==sign(arr[j])){
                cur = max(ll(cur),arr[j]);
                j++;
           }
           sum+=cur;
           i=j-1;
        }
        cout<<sum<<endl;
        
    }
    return 0;
}