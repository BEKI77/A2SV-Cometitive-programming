class Solution {
public:
    vector<vector<string>> findDuplicate(vector<string>& paths) {
        int n = paths.size();
        unordered_map<string,vector<string>> store;
        vector<vector<string>> res;
        for(int i=0; i<n; i++){
            string directoryinfo = paths[i];
            stringstream ss(directoryinfo);
            string s, dirName;
            bool first = true;
            
            while(getline(ss,s,' ')){
                if(first){
                    dirName = s;
                    first = false;
                }else{
                    int fileNameLen=0, i=0;
                    while(i < s.size() && s[i++]!='(') fileNameLen++;
                    string fileName = s.substr(0,fileNameLen);
                    
                    int fileLen=0, j=0;
                    while(j < s.size() && s[j++] != ')') fileLen++;
                    string fileCon = s.substr(fileNameLen+1, fileLen);
                    
                    store[fileCon].push_back(dirName+"/"+fileName);
                }
            }
        }
        
        for(auto [con, dirFile]: store){
            if(dirFile.size()>1){
                res.push_back(dirFile);
            } 
        }
        return res;
        }
};
