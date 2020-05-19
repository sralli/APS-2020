#include <iostream>
using namespace std;

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n; 
        cin>>n;
        int arr[n];
        int ans=0, odd=0;
        int nxt_index;
        for(int i=0; i<n; i++)
        {
            cin>>arr[i];

        }

        for (int i=0; i<n; i++)
        {
            if (arr[i]&1)
                odd++;

            if (arr[i]%4==0)
                {
                    ans += (n-i) + ((odd * (odd + 1)) / 2) + (odd * (n-i));
                    odd = 0;
                }
            if (arr[i]%4==2)
            {
                nxt_index=n;
                for (int j=i+1; j<=n;j++)
                {
                    if (arr[j]%2==0)
                    {
                        nxt_index=j;
                        break;
                    }
                }

                ans += (n-nxt_index) + ((odd * (odd + 1)) / 2) + (odd * (n-nxt_index));
                odd=0;
            }

           
           
        }
        ans += (odd * (odd + 1)) / 2;
        cout<<int(ans)<<"\n";
    }
}
