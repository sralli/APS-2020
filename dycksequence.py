import math
from itertools import permutations
N=int(input())
catalan = math.factorial(2*N)//(math.factorial(N+1)*math.factorial(N))
l=[]
count=0
for i in range(0,N):
	l.append('x')
	l.append('y')
per = list(permutations(l))
per=list(set(per))
for i in range(0,len(per)):
	s=''
	flag=0
	for j in range(0,len(per[i])):
		s=s+per[i][j]
		if s.count('x') < s.count('y'):
			flag=1
			break
	if flag==0:
		print(per[i])
		count+=1
		if count>=catalan:
			break
