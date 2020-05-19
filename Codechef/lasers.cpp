#include<bits/stdc++.h> 
using namespace std; 
  
struct Query 
{ 
    int l, r, x, idx; 
}; 

struct ArrayElement 
{ 
    int val, idx; 
}; 
  

bool cmp1(Query q1, Query q2) 
{ 
    return q1.x < q2.x; 
} 
  
/
bool cmp2(ArrayElement x, ArrayElement y) 
{ 
    return x.val < y.val; 
} 
  

void update(int bit[], int idx, int val, int n) 
{ 
    for (; idx<=n; idx +=idx&-idx) 
        bit[idx] += val; 
} 
  

int query(int bit[], int idx, int n) 
{ 
    int sum = 0; 
    for (; idx > 0; idx -= idx&-idx) 
        sum += bit[idx]; 
    return sum; 
} 
  
void answerQueries(int n, Query queries[], int q, 
                              ArrayElement arr[]) 
{  
    int bit[n+1]; 
    memset(bit, 0, sizeof(bit)); 
  
  
    sort(arr, arr+n, cmp2); 
  
   
    sort(queries, queries+q, cmp1); 
  
  
    int curr = 0; 
  
 
    int ans[q]; 
  
 
    for (int i=0; i<q; i++) 
    { 
     
        while (arr[curr].val <= queries[i].x && curr<n) 
        { 
           
            update(bit, arr[curr].idx+1, 1, n); 
            curr++; 
        } 
  
        
        ans[queries[i].idx] = query(bit, queries[i].r+1, n) - 
                              query(bit, queries[i].l, n); 
    } 
  
    // printing answer for each Query 
    for (int i=0 ; i<q; i++) 
        cout << ans[i] << endl; 
} 




  int main()
  {
      int t;
      cin>>t;
      while(t--)
      {
          int n,m;
          cin>>n>>m;
          int arr[n+1];
          unsigned arr2[n-1];
          int temp;
          for(int i=1; i<=n; i++)
          {
              cin>>arr[i]     
          }
          
          for(int i=0; i<n; i++)
          {
              arr2[i] = arr[i+1]-arr[i]
          }

          for(int i=0; i<n;i++)
          {
              cout<<arr2[i];
          }


          while(m--)
          {
              int q[3];
              for(int i=0; i<3; i++)
              {
                  cin>>q[i];
              }
              int c=0;

              for(int i=0; i<=n; i++)
              {
                  
                 // cout<<p[i]<<arr[i]<<p[i+1]<<arr[i+1];
                  struct Point p1= {p[i], arr[i]}, q1 = {p[i+1], arr[i+1]};
                  struct Point p2 = {q[0],q[2]}, q2 = {q[1], q[2]};

                  if (doIntersect(p1, q1, p2, q2))
                  {
                      c++;
                    

                      if (p[i]==q[1] && arr[i]==q[2])
                        c-=1;
                      else if (p[i+1]==q[0] && arr[i+1]==q[2])
                        cout<<p[i+1]<<q[0]<<arr[i+1]<<q[2];
                         c-=1;
                      

                  }

              }
              cout<<c<<'\n';
          }
      }
  }