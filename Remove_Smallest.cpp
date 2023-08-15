#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL), cout.tie(NULL);
    int t;
    cin>>t;

    while(t--) {
        int n;
        cin>>n;
        vector<int> arr(n);
        for(int i=0; i<n; i++) cin>>arr[i];
        sort(arr.begin(), arr.end());
        bool ans = true;
        for(int i=0; i<n-1; i++){
            if(abs(arr[i]-arr[i+1])>1) ans=false;   
        }
       cout<<(ans ? "YES" : "NO")<<"\n";
    }
    return 0;
}