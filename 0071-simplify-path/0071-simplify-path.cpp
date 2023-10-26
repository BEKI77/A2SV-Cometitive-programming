class Solution {
public:
    string simplifyPath(string path) {
        stack<string> dir;
        string res;
        for(int i=0; i<path.length(); i++){
            if(path[i]=='/') continue;
            string temp;
            while(i<path.length() && path[i]!='/'){
                temp+=path[i];
                i++;
            }
            if(temp=="."){
                continue;
            }else if(temp==".."){
                if(!dir.empty()){
                    dir.pop();
                }
            }else{
                dir.push(temp);
            }
        }
        
        while(!dir.empty()){
            res="/"+dir.top()+res;
            dir.pop();
        }
        return res==""? "/":res;
    }
};