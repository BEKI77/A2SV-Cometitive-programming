#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL); cout.tie(NULL);
    int n;
    bool ex[2];
    cin>>n;
    vector<int> arr(n);
    for(int i=0; i<n; i++) {
        cin>>arr[i];
        ex[arr[i]%2]=1;
    }

    if(ex[0]&&ex[1]) sort(arr.begin(), arr.end());
    //the above implementation takes nlogn(0)

    /*for(int i=0; i<n; i++){
        bool chk=0;
        for(int j = 0; j<n; j++){
            if((arr[i]+arr[j])%2!=0){
                sort(arr.begin(), arr.end());
                chk=1;
                break;
            }
        }
        if(chk) break;
    }
    */
   //the above implementation takes n`2(0)
   
    for(int i=0; i<n; i++) cout<<arr[i]<<" ";

    return 0;
}