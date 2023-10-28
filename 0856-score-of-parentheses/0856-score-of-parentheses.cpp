class Solution {
public:
    int scoreOfParentheses(string s) {
        stack<int> st;
        int val=0, ans=0;
        for(int i=0; i<s.length(); i++){
            char temp = s[i];
            if(temp=='('){
                st.push(0);
            }else{
                int mul = st.top();
                st.pop();
                if(mul==0){
                    val=1;
                }else{
                    val = mul*2;
                }
                
                if(st.empty()){
                    ans+=val;
                }else{
                    int cur= st.top()+val;
                    st.pop();
                    st.push(cur);
                }
            }
        }
        
        return ans;
    }
};