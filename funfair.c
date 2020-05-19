#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include<limits.h>

int min(int x, int y) { return (x < y)? x: y; } 
  
int RMQ(int segtree[],int query_l,int query_h,int low,int high,int pos)
{
    if(query_l <= low && query_h >= high)
    {
        return segtree[pos];
    }
    if(query_l > high || query_h < low)
    {
        return INT_MAX;
    }
    int mid = (low + high)/2;
    return min(RMQ(segtree,query_l,query_h,low,mid,2*pos + 1),RMQ(segtree,query_l,query_h,mid + 1,high,2*pos + 2));
}
void buildtree(int a[],int segtree[],int pos, int low, int high)
{
    if(low == high)
    {
        segtree[pos] = a[low];
        return ;
    }
 
        int mid = (low + high)/2;
        buildtree(a,segtree,2*pos + 1,low,mid);
        buildtree(a,segtree,2*pos + 2,mid + 1,high);
        segtree[pos] = min(segtree[2*pos + 1],segtree[2*pos + 2]);
}



int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    int n, m;
    n = scanf("%d", &n);
    m = scanf("%d", &m);
    
    int i =0;
    int arr[n];
    
    
    
    for(i=0; i<=m; i++)
    {
        arr[i]=scanf("%d", &i);
    }
    
    int x = (int)(ceil(log2(n)));
    int siz = 2*(int)pow(2,x) - 1;
    int segtree[siz];
    int pos = 0;
    int low = 0;
    int high = n - 1;
    buildtree(arr,segtree,pos,low,high);
    
    
    int j=0;
    int qs, qe;
    
    for(j=0; j<=m; j++)
    {
        qs = scanf("%d", &qs);
        qe = scanf("%d", &qe);
        printf("%d", RMQ(segtree,qs,qe,0,n-1,0));
    }
    
    
    
    
    
}
