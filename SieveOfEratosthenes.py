def SieveOfEratosthenes(n):
	val=[]
	prime = [True for i in range(n+1)]
	p = 2
	while(p * p <= n): 
		if (prime[p] == True): 
			for i in range(p * 2, n + 1, p): 
				prime[i] = False
		p += 1
	c = 0
	count=0
	for p in range(2, n): 
		if prime[p]: 
			c += 1
			count+=p
			val.append(p)
	print(val)
	return count
n=2*1000000
c = SieveOfEratosthenes(n) 
print(c)
