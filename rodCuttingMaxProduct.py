N=int(input())
result=[0]*(N+1)
print(result)
for i in range(2,N+1):
	for j in range(1,(i//2)+1):
		val=(j*(i-j))
		val1=(j*result[(i-j)])
		result[i]=max(result[i],val,val1)
print(result)
