def next(a,b):
	d=[]
	for i in range(21,100):
		if i%10!=0:
			c=a[i//10]+b[i%10]
			d.append(c)
		else:
			d.append(a[i//10])
	return(d)

val="onetwothreefourfivesixseveneightnineteneleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteentwenty"
a=["zero","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
b=["zero","one","two","three","four","five","six","seven","eight","nine","ten"]
e=["eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty"]
d=[]
val1="hundredand"
for i in range(0,10):
	b.append(e[i])
print(b)
d=next(a,b)
f=[]
print(d)
d.append("hundred")
for i in range(0,len(d)):
	b.append(d[i])
print(b)
for i in range(1,len(b)):
	f.append(b[i])
print(b[100])
for i in range(101,1000):
	if i%100!=0:
		k=b[i//100]+val1+b[i%100]
	else:
		print("Hi")
		k=b[i//100]+b[100]
	f.append(k)
f.append("thousand")
print(f)
newval=0
for i in range(0,len(f)):
	newval+=len(f[i])
print(newval)
vall=0
while(1):
	n=int(input())
	for i in range(0,n):
		vall+=len(f[i])
	print(vall)
