def heapify(A):
	A.insert(0,0)
	bit=0
	while(bit!=1):
		bit=1
		for i in range(((len(A)-1)//2),0,-1):
			if (2*i)<len(A):
				if A[i]>A[2*i]:
					A[i],A[2*i]=A[2*i],A[i]
					bit=0
			if  (2*i)+1<len(A):
				if A[i]>A[(2*i)+1]:
					A[i],A[(2*i)+1]=A[(2*i)+1],A[i]
					bit=0
	A.pop(0)
	return A
A=list(map(int,input().split()))
B=[]
for i in range(0,len(A)):
	heapify(A)
	B.append(A.pop(0))
print(B)
