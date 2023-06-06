#include <iostream>
     int main()
     {
        long long int  m,n,a;
         long long int d1,d2;
         std::cin>>m>>n>>a;
         if (m%a==0)
         d1=0;
         else
         d1=1;
       if(n%a==0)
         d2=0;
         else
         d2=1;
         
       long long int temp= ((m/a)+d1)*((n/a)+d2);
         std::cout<<temp;
         return 0;
     }
