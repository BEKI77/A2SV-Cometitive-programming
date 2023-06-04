vector<int> countingSort(vector<int> arr) {
   int n = 100;
   cout<<n<<endl;
   vector<int> newArr(n);
   for(int i=0; i<arr.size(); i++){
       newArr[arr[i]]=newArr[arr[i]]+1;
   }
   return newArr;
}
