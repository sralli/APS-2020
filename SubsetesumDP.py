def findSubset(A,N):
	M=[]
	l=[]
	l.append(True)
	for i in range(1,N+1):
		if A[0]==i:
			l.append(True)
		else:
			l.append(False)
	M.append(l)
	for i in range(1,len(A)):
		l=[]
		for j in range(0,N+1):
			if A[i]>j:
				l.append(M[i-1][j])
			elif M[i-1][j]==True:
				l.append(True)
			elif M[i-1][j-A[i]]==True:
				l.append(True)
			else:
				l.append(False)
		M.append(l)
	for i in M:
		print(i)
A=list(map(int,input().split()))
N=int(input())
A.sort()
findSubset(A,N)
