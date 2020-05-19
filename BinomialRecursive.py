N=int(input())
K=int(input())
def Binomial(n,k):
	if n==k or k==0:
		return 1
	return Binomial(n-1,k-1)+Binomial(n-1,k)
print(Binomial(N,K))
