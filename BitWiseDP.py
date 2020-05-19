import sys
def countSetBits(n):
	count=0
	while(n!=0):
		n=n&(n-1)
		count+=1
	return count
def countSetBitsPrakashSir(n):
	count=0
	while(n):
		count+=n&1
		n>>=1
	return count
def countSetBitsVibha(n):
	count=list(map(int,bin(n)[2:]))
	return sum(count)
n=int(input())
cost=[]
for i in range(0,n):
	A=list(map(int,input().split()))
	cost.append(A)
dp=[sys.maxsize for i in range(2**n)]
dp[0]=0
for i in range(0,2**n):
	count=countSetBitsVibha(i)
	if count==n:
		break
	for j in range(0,n):
		if i&(1<<j)==1:
			continue
		else:
			val = i|(1<<j)
			dp[val]=min(dp[val],dp[i]+cost[count][j])
print(dp)
print(dp[(2**n)-1])
