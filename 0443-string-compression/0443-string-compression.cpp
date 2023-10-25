class Solution {
public:
    int compress(vector<char>& chars) {
        string s ="";
        int ans;
        if(chars.size()<=1) return 1;
        for(int i=0; i<chars.size(); i++){
            int cnt=1, r=i;
            string temp="";
            while(r+1<chars.size() && chars[i]==chars[r+1] ){
                cnt++;
                r++;
            }
            if(cnt==1){
                temp=chars[i];
            }else{
                temp = chars[i]+to_string(cnt);
            }
            s+=temp;
            i=r;
        }
        cout<<s;
        for(int i=0; i<s.length(); i++) chars[i]=s[i];
        
        return s.length();
    }
};