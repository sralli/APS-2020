#include<stdio.h>
void swap(int *a,int *b)
{
int temp;
temp=*a;
*a=*b;
*b=temp;
}
void quick_sort(int *a,int first,int last)
{
printf("\n");
for(int i=first;i<=last;i++)
{
printf("%d\t",a[i]);
}
printf("\nBye\n");
int i,j,pivot;
if(first<last)
{
	i=first;
	j=last;
	pivot=first;
	while(i<=j)
	{
		while(i<=last && a[i]<=a[pivot])
			i++;
		while(j>=first && a[j]>a[pivot])
			j--;
		if(i<j)
			swap(&a[i],&a[j]);
	}
	swap(&a[j],&a[pivot]);

quick_sort(a,first,j-1);
quick_sort(a,j+1,last);
}
}
int main()
{
int a[20];
int n;
printf("\n Enter the total number of entries:");
scanf("%d",&n);
printf("\n Enter the array:");
for(int i=0;i<n;i++)
{
scanf("%d",&a[i]);
}
quick_sort(a,0,n-1);
for(int i=0;i<n;i++)
{
printf("%d\n",a[i]);
}
return(0);
}
