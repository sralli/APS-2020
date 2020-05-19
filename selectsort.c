#include<stdio.h>
#include<time.h>
#include<stdlib.h>
long long count_bubble=0;
long long count_select=0;
long long count_insertion=0;
void heapsort(*a,int n)
{
int l,r;
for(int i=0;i<n;i++)
{
l=2*i+1;
r=2*i+2;
if(l<n && r<n)
{
	if(a[l]>a[i])
	{
		swap(&a[i],&a[l]);
	}
	else
	{
		swap(&a[i],&a[r]);
	}

}
}
}
void insertion(int *a,int n)
{
int j;
int key;
long long k=0;
long long d=0;
for(int i=1;i<n;i++)
{
	d++;
	key=a[i];
	j=i-1;
	while(j>=0 && key<a[j])
	{
		k++;
		a[j+1]=a[j];
		j=j-1;
		/*for(int i=0;i<n;i++)
		{
			printf("%d\t",a[i]);
		}
		printf("\n");*/		
	}
	a[j+1]=key;
}
for(int i=0;i<n;i++)
		{
			printf("%d\n",a[i]);
		}
		printf("\n");
count_insertion=k;
}
void bubblesort(int *a,int n)
{
long long k=0;
long long d=0;
int temp;
for(int i=0;i<n;i++)
{
d++;
for(int j=i+1;j<n;j++)
{
k++;
if(a[i]>a[j])
{
temp=a[i];
a[i]=a[j];
a[j]=temp;
}
}
}
count_bubble=k;
}
void selectsort(int *a,int n)
{
int mini;
int temp;
long long d=0;
long long k=0;
for(int i=n-1;i>0;i--)
{
d++;
mini=i;
for(int j=i;j>=0;j--)
{
k++;
	if(a[j]>a[mini])
	{
		mini=j;
	}
}
temp=a[i];
a[i]=a[mini];
a[mini]=temp;
/*printf("\n------\n");
for(int i=0;i<n;i++)
{
printf("%d\t",a[i]);
}*/
}
for(int i=0;i<n;i++)
{
printf("%d\n",a[i]);
}
count_select=k;
}
int main()
{
int temp;
int mini;
int n;
int ch;
time_t t;
printf("\n Enter the number of elements:");
scanf("%d",&n);
int a[n];
int b[n];
int key;
printf("\n Enter the array:");
srand((unsigned) time(&t));
for(int i=0;i<n;i++)
{
 //key=rand()%500;
//a[i]=key;
scanf("%d",&a[i]);
}
for(int i=0;i<n;i++)
{
b[i]=a[i];
}
do
{
printf("\n 1.Bubblesort\n2.Selectionsort\n3.Insertionsort");
printf("\n Enter the choice:");
scanf("%d",&ch);
switch(ch)
{
case 1:
bubblesort(a,n);
printf("Number of comparisions=%lld",count_bubble);
count_bubble=0;
break;
case 2:
selectsort(a,n);
printf("\nNumber of comparisions=%lld",count_select);
count_select=0;
break;
case 3:
insertion(a,n);
printf("\nNumber of comparisions=%lld",count_insertion);
count_insertion=0;
break;
default :
break;
}
/*printf("\n---A---\n");
for(int i=0;i<n;i++)
{
printf("%d\n",a[i]);
}
*/
for(int i=0;i<n;i++)
{
a[i]=b[i];
}
}while(ch<4);
printf("\n---A---\n");
for(int i=0;i<n;i++)
{
printf("%d\n",a[i]);
}
printf("\n---B---\n");
for(int i=0;i<n;i++)
{
printf("%d\n",b[i]);
}
return(0);
}
