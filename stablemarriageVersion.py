T=int(input())
l=[]
for i in range(0,T):
	a=list(map(int,input().split()))
	l.append(a)
m=[]
f=[]
m.append(-1)
for i in range(0,T):
	m.append(0)
	f.append(0)
for i in range(0,T):
	for j in range(0,T):
		if l[i][j]!=-1:
			if m[l[i][j]]==0 and f[i]==0 :
				m[l[i][j]]=1
				f[i]=1
flag=0
for i in range(1,len(m)):
	if m[i]!=1:
		print(i)
		flag=1
if flag==0:
	print(-1)
