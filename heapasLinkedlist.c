#include<stdio.h>
#include<stdlib.h>
typedef struct node
{
int data;
int index;
struct node *next;
}NODE;
NODE *head,*pre;
int cnt=0;
NODE * find(int a)
{
NODE *temp=head;
while(temp->index!=a)
temp=temp->next;
return(temp);
}
void swap(int *a,int *b)
{
int temp;
temp=*a;
*a=*b;
*b=temp;
}
int max(int *a,int *b)
{
if(*a>*b)
return(*a);
else
return(*b);
}
void heapify(int n)
{
int count=1;
int i;
NODE *temp;
NODE *temp1,*temp2;
while(count!=0)
{
	i=n/2;
	count=0;
	while(i>0)
	{
		temp2=find(2*i);
		temp=find(i);
		if(2*i+1<=n)
		{
		temp1=find(2*i+1);
			if(temp->data<temp1->data||temp->data<temp2->data)
				{
					if(temp->data<temp2->data)
						swap(&temp->data,&temp2->data);
					else
						swap(&temp->data,&temp1->data);
					count++;
				}
		}
		else if(temp->data<temp2->data)
			{
				swap(&temp->data,&temp2->data);
				count++;
			}
		i--;
	}
}
}
void heapsort(int n)
{
NODE *temp,*temp1;
temp=find(1);
for(int i=1;i<=n;i++)
	{		
		temp1=find(n-i+1);
		heapify(n-i+1);
		swap(&temp->data,&temp1->data);
	}
}
void insert(int key)
{
cnt++;
NODE *p;
p=malloc(sizeof(NODE));
p->data=key;
p->index=cnt;
p->next=NULL;
if(head==NULL)
{
head=p;
}
else
{
pre->next=p;
}
pre=p;
}
void disp()
{
NODE *temp;
temp=head;
while(temp!=NULL)
{
printf("%d\n",temp->data);
temp=temp->next;
}
}
int main()
{
int key;
int n;
printf("Enter the number of elements in array:");
scanf("%d",&n);
printf("Enter the elements in array:");
for(int i=1;i<=n;i++)
	{
		scanf("%d",&key);
		insert(key);
	}
heapsort(n);
disp();
return(0);
}
