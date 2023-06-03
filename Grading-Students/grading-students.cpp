vector<int> gradingStudents(vector<int> grades) {
  vector<int> rounded;
     for(float i: grades){
         if(i<38){
            rounded.push_back(i);
         }else if((ceil(i/5)*5 - i) < 3){
            rounded.push_back((ceil(i/5)*5));
         }else{
             rounded.push_back(i);
         }
    }
  return rounded;
}
