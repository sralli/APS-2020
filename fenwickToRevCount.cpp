#include<bits/stdc++.h> 
using namespace std; 
long long  getSum(long long  BITree[], long long  index) 
{ 
    long long  sum = 0; 
    while (index > 0) 
    { 
        sum += BITree[index]; 
        index -= index & (-index); 
    } 
    return sum; 
} 
void updateBIT(long long  BITree[], long long  n, long long  index, long long  val) 
{ 
    while (index <= n) 
    { 
    BITree[index] += val; 
    index += index & (-index); 
    } 
} 
void convert(long long  arr[], long long  n) 
{ 
    long long  temp[n]; 
    for (long long  i=0; i<n; i++) 
        temp[i] = arr[i]; 
    sort(temp, temp+n); 
    for (long long  i=0; i<n; i++) 
    { 
        arr[i] = lower_bound(temp, temp+n, arr[i]) - temp + 1; 
    } 
} 
long long  getInvCount(long long  arr[], long long  n) 
{ 
    long long  invcount = 0;     
    convert(arr, n); 
    long long  BIT[n+1]; 
    for (long long  i=1; i<=n; i++) 
        BIT[i] = 0;     
    for (long long  i=n-1; i>=0; i--) 
    { 
        invcount += getSum(BIT, arr[i]-1); 
        updateBIT(BIT, n, arr[i], 1); 
    }
    return invcount; 
}
int main() 
{
    long long T;
    cin>>T;
    for(long long w=0;w<T;w++)
    {
    long long N;
    cin>>N;
    long long  arr[N];
    long long count=0;
    for(long long i=0;i<N;i++)
    {
        cin>>arr[i];
    }
    long long n = sizeof(arr)/sizeof(long long ); 
        count=getInvCount(arr,n);
    cout<<count<<"\n";
    if(count>=N)
    {
        cout<<"YES"<<"\n";
    }
    else
    {
        cout<<"NO"<<"\n";
    }
    }
    return 0; 
} 
