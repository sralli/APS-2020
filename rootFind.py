def root(a,i):
	while(a[i]!=i):
		i=a[i]
	return i
def find(a,u,v):
	if root(a,u) == root(a,v):
		return 1
	else:
		return 0
def union(a,u,v):
	rootu=root(a,u)
	rootv=root(a,v)
	a[rootu]=rootv
A=list(map(int,input().split()))
union(A,0,1)
union(A,0,5)
union(A,3,4)
union(A,5,4)
union(A,1,6)
find(A,3,6)
print(A)
