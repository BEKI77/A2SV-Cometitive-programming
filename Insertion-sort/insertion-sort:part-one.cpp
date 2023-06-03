void insertionSort1(int n, vector<int> arr) { 
    int temp=arr[n-1];
    for(int i = n-1; i >= 0; i --){
        if(arr[i-1]>temp){
            arr[i]=arr[i-1];
            for(int j = 0; j<n; j++){
                std::cout<<arr[j]<<" ";
            }
            std::cout<<std::endl;
        }else{
            arr[i]=temp;
            for(int j=0; j<n;j++){
                std::cout<<arr[j]<<" ";
            }
            break;
        }
    }

}
