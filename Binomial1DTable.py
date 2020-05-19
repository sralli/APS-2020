N=int(input())
K=int(input())
C=[]
for i in range(0,N+1):
	C.append(0)
C[0]=1
z=1
for i in range(1,N+1):
	for j in range(min(i,K),0,-1):
		C[j]+=C[j-1]
print(C[K])
