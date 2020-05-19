def Union(A,u,v):
	val=A[v]
	val1=A[u]
	for i in range(0,len(A)):
		if A[i]==val1:
			A[i]=val
def Find(A,u,v):
	for i in range(0,len(A)):
		print(A[u],A[v])
		if A[i]==A[u] and A[i]==A[v]:
			return 1
	return 0
E=int(input())
N=int(input())
B=[]
for i in range(0,N):	
	A=list(map(int,input().split()))
	B.append(A)
A=[]
for i in range(0,E+1):
	A.append(i)
B.sort()
c=[]
for i in range(0,N):
	if not Find(A,B[i][1],B[i][2]):
		Union(A,B[i][1],B[i][2])
		c.append(B[i])
print(c)
