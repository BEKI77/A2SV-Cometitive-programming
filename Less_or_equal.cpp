#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(NULL);	cout.tie(NULL);
	int n, k, cnt=0;
	cin>>n>>k;
	vector<ll> arr(n);
	
	for(int i=0; i<n; i++) cin>>arr[i];
	
	sort(arr.begin(), arr.end());
	
	ll ans;

	if(k==0) ans = arr[0] -1;
	else ans = arr[k-1];
	
	for(int i =0; i<n; i++) if(arr[i]<=ans) cnt++;

	cout<<(cnt!=k || !(1<=ans && ans <= 1000*1000*1000)? -1: ans);
	
	return 0;
}
