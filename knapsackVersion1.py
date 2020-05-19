T=int(input())
val=[]
for i in range(0,T):
	A=list(map(int,input().split()))
	val.append([A[1],A[0],i])
M=int(input())
l=[]
for i in range(0,len(val)):
	l.append([(val[i][0]/val[i][1]),val[i][2]])
l.sort(key=lambda x:x[0],reverse=True)
print(l)
W=[]
P=[]
value=0
for i in range(0,len(l)):
	W.append(val[l[i][1]][1])
	P.append(val[l[i][1]][0])
for i in range(0,len(val)):
	if(M>0 and W[i]<=M):
		M=M-W[i]
		value+=P[i]
	else:
		break
if M>0:
	value+=P[i]*(M//W[i])
print(value)
