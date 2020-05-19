T=int(input())
for _ in range(0,T):
	N=int(input())
	flag=0
	for i in range(2,N//2+1):
		if N%i==0:
			flag=1
			break
	if flag==0:
		print("yes")
	else:
		print("no")
