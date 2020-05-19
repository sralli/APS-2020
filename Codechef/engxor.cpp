
#include <iostream> 
using namespace std;
  
 
#define P2(n) n, n ^ 1, n ^ 1, n 
#define P4(n) P2(n), P2(n ^ 1), P2(n ^ 1), P2(n) 
#define P6(n) P4(n), P4(n ^ 1), P4(n ^ 1), P4(n) 
#define LOOK_UP P6(0), P6(1), P6(1), P6(0) 
  
unsigned int table[256] = { LOOK_UP }; 
  

inline int getParity(int num) 
{ 
   
    int max = 16; 
  
    while (max >= 8) { 
        num = num ^ (num >> max); 
        max = max / 2; 
    } 
  
   
    return table[num & 0xff]; 
} 
  

int main()
{
    ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int t;
    cin>>t;
    while(t--)
    {
        int n, q;
        cin>>n>>q;
        long long odd=0, even=0;
        int temp;
        for(int i=0; i<n;i++)
        {
            cin>>temp;
            if (getParity(temp)!=0)
                even++;
            else
                odd++;

        }

        while(q--)
        {
            cin>>temp;
            int result;
            result = getParity(temp);
            result ? cout <<even<<" "<<odd<<"\n": 
             cout <<odd<<" "<<even<<"\n"; 
    

        }

    

    }

    return 0;
}