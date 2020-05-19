def prime(m):
	if(m==1):
		return(False)
	for i in range(2,m):
		if(m%i==0):
			return(False)
	return(True)
def primes(n):
	p=[]
	c=0
	i=2;
	while(c<n):
		if prime(i):
			p=p+[i]
			c=c+1;
		i=i+1;
	return(p)
