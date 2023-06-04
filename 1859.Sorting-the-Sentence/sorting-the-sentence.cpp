class Solution {
public:
    string sortSentence(string s) {
      string newStr;
      vector < string > strings;
      char separator = ' ';
      int startIndex = 0, endIndex = 0;
        // This loop is for separating
         for (int i = 0; i <= s.size(); i++) {
               // If we reached the end of the word or the end of the input.
                if (s[i] == separator || i == s.size()) {
                   endIndex = i;
                   string temp;
                   temp.append(s, startIndex, endIndex - startIndex);
                   strings.push_back(temp);
                  startIndex = endIndex + 1;}
          }
        // This loop is for sorting
         for (int i=0; i<strings.size(); i++){ 
             for(int j = 0; j < strings.size()-1; j++){ 
                 int val = strings[j].size()-1;
               if(strings[j][val] > strings[j+1][strings[j+1].size()-1]){
                    swap(strings[j], strings[j+1]);
               }
           }
        }
        // This loop is for joining the sorted strings
        for(int i =0; i < strings.size(); i++){
                strings[i][strings[i].size()-1]=separator;
                newStr += strings[i];    
        }
        // To remove the last space
       newStr.pop_back();
      return newStr;
    }
};
