class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> st;
        for(int i=0; i<tokens.size(); i++){
            string temp = tokens[i];
            if(temp=="+"){
                int sec = st.top();
                st.pop();
                int fir = st.top();
                st.pop();
                st.push(fir+sec);
            }else if(temp=="-"){
                int sec = st.top();
                st.pop();
                int fir = st.top();
                st.pop();
                st.push(fir-sec);
            }else if(temp=="*"){
                int sec = st.top();
                st.pop();
                int fir = st.top();
                st.pop();
                st.push(fir*sec);
            }else if(temp=="/"){
                int sec = st.top();
                st.pop();
                int fir = st.top();
                st.pop();
                st.push(fir/sec);
            }else{
                st.push(stoi(temp));
            }
        }
        
        return st.top();
    }
};