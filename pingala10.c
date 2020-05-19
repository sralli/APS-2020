#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
int main()
{
int n;
scanf("%d",&n);
long long c=1;
long long a=0;
long long b=1;
int j=3;
long long d[100];
d[1]=0;
d[2]=1;
for(int i=2;i<=n;i++)
{
    c=a+b;
    a=b;
    b=c;
    d[j++]=c;
}
int p,q;
scanf("%d",&p);
scanf("%d",&q);
long long sum=0;
if(p==1)
sum=2;
if(p==2)
sum=1;
for(int i=p;i<=q;i++)
{
    if(d[i]==2)
        sum+=2;
    if(d[i]==3)
        sum+=3;
    if(i==6)
        sum+=d[i];
    if(i==8)
        sum+=d[8];
    if(i==12)
        sum+=d[12];
    if(i==14)
        sum+=d[14];
    if(i==18)
        sum+=d[18];
    if(i==24)
        sum+=d[24];
    if(i==30)
        sum+=d[30];
    if(i==44)
        sum+=d[44];
    if(i==48)
        sum+=d[48];
}
printf("%lld\n",sum);
return(0);
}
