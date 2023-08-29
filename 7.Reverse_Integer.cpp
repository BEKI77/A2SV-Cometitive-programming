class Solution {
public:
    int reverse(int x) {
        long int ans=0;
	while(x){
		r=r*10+x%10;
		x\=10;
    	}
	return (r > INT_MAX || r < INT_MIN ? 0: r);
};
