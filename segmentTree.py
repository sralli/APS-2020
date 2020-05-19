import sys
import math
sys.setrecursionlimit(10000000)
def createTree(a,stree,low,high,pos):
	if low==high:
		stree[pos]=a[low]
		return
	mid=(low+high)//2
	createTree(a,stree,low,mid,(2*pos)+1)
	createTree(a,stree,mid+1,high,(2*pos)+2)
	stree[pos]=min(stree[(2*pos)+1],stree[(2*pos)+2])
def minQuery(stree,qlow,qhigh,low,high,pos):
	if qlow<=low and qhigh>=high:
		return stree[pos]
	if qlow>high or qhigh<low:
		return sys.maxsize
	mid=low+(high-low)//2
	return min(minQuery(stree,qlow,qhigh,low,mid,(2*pos)+1),minQuery(stree,qlow,qhigh,mid+1,high,(2*pos)+2))
A=list(map(int,input().split()))
Q=int(input())
n=len(A)
val=int(math.ceil(math.log2(n)))
val1=2*(2**val)-1
stree=[sys.maxsize]*val1
print(stree)
print(n)
createTree(A,stree,0,n-1,0)
print(stree)
	for i in range(Q):
		l,r=map(int,input().split())
		print(minQuery(stree,l,r,0,n-1,0))
	
