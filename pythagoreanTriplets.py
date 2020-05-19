def pythagoreanTriplets(limits): 
	c,m =0,2
	while c<limits: 
		for n in range(1, m): 
			a=m*m-n*n 
			b=2*m*n 
			c=m*m+n*n 
			if c>limits: 
				break
			print(a, b, c)
			if a+b+c==1000:
				print("hello")
				print(a+b+c," ",a,b,c)
		m=m+1
while(1):
	limit = int(input())
	pythagoreanTriplets(limit) 
