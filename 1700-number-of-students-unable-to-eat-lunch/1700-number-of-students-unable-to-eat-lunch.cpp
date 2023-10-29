class Solution {
public:
    int countStudents(vector<int>& students, vector<int>& sandwiches) {
        int n = students.size(), cntmo=0;
        queue<int> st;
        stack<int> sa;
        for(int i=0; i<n; i++){
            st.push(students[i]);
            sa.push(sandwiches[n-i-1]);
        }
        
        while(!st.empty()){
            if(st.front()==sa.top()){
                st.pop();
                sa.pop();
                cntmo=0;
            }else{
                int temp = st.front();
                st.pop();
                st.push(temp);
                cntmo++;
                if(cntmo==n){
                    return st.size();
                }
            }
        }
        
        return st.size();
    }
};