#include <bits/stdc++.h>
using namespace std;

class Solution {
	public:
	vector<string> subdomainVisits(vector<string>& cpdomains) {
		unordered_map<string, int> count;

        	for (auto cd : cpdomains) {
           		int i = cd.find(" ");
            		int n = stoi(cd.substr (0, i));
            		string s = cd.substr (i + 1);
            		for (int i = 0; i < s.size(); ++i)
                		if (s[i] == '.')
                    			count[s.substr(i + 1)] += n;
            	count[s] += n;
        	}

        	vector<string> res;
        
		for (auto k : count)
            		res.push_back (to_string(k.second) + " " + k.first);
        	
		return res;
	}
};

int main() {
	Solution sol;
	vector<string> q;
	q.push_back("9001 discuss.leetcode.com");
	q.push_back("900 google.mail.com");
	q.push_back("50 yahoo.com");
	q.push_back("1 intel.mail.com");
	q.push_back("5 wiki.org");
	vector<string> ans = sol.subdomainVisits(q);

	for(int i=0; i<ans.size(); i++) cout<<ans[i]<<endl;

	return 0;
}
