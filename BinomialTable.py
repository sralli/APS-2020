N=int(input())
K=int(input())
C=[[0]*(K+1) for i in range(N+1)]
'''
for i in range(0,N+1):
	l=[]
	for j in range(0,K+1):
		l.append(0)
	C.append(l)
'''
for i in range(0,N+1):
	for j in range(0,min(i+1,K+1)):
		if j==0 or i==j:
			C[i][j]=1
		else:
			C[i][j]=C[i-1][j-1]+C[i-1][j]
print(C[i][K])
