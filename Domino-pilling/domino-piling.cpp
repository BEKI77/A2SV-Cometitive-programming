#include <iostream>
#include <cmath>
using namespace std;
         
int main()
{
       float dominos_area = 2*1;
       float square_area;
       int  m,n;
       cin>>m>>n;
       square_area = m*n;
       cout<< floor(square_area/dominos_area);
     
  return 0;
}
