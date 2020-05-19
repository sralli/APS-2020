d={'&':[[[0,0],[0,1],[0,2],[0,3],[1,0],[2,0],[3,0],[2,3],[3,2]],[[1,1]],[[2,1],[1,2],[2,2]],[[1,3],[3,1],[3,3]]],'^':[[[0,0],[2,2],[1,1],[3,3]],[[0,1],[1,0],[2,3],[3,2]],[[0,2],[2,0],[1,3],[3,1]],[[0,3],[1,2],[2,1],[3,0]]],'|':[[[0,0]],[[0,1],[1,0],[1,1],[1,2],[1,3],[2,1],[2,3],[3,1],[3,2]],[[0,2],[2,0],[2,2]],[[0,3],[3,0],[3,3]]]}
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
def power(x, n, m):
    x%=m;
    res=1;
    while(n!=0):
        if((n&1)==1):
            res=(res*x)%m;
        x=(x*x)%m;
        n>>=1;
    return res;
	
def precedence(op): 
	if op == '&': 
		return 3
	if op == '|': 
		return 1
	if op == '^':
		return 2
	return 0
def applyOp(a, b, op): 
	val=d[op]
	l=[]
	for i in range(4):
		val1=0
		for j in range(len(val[i])):
			val1+=a[val[i][j][0]]*b[val[i][j][1]]
		l.append(val1)
	return l
def evaluate(tokens): 
	values = [] 
	ops = [] 
	i = 0
	while i < len(tokens): 
		if tokens[i] == ' ': 
			i += 1
			continue
		elif tokens[i] == '(': 
			ops.append(tokens[i])
		elif tokens[i] == '#':
			values.append([1,1,1,1])
			i+=1
			continue 
		elif tokens[i].isdigit(): 
			val = 0
			while (i < len(tokens) and
				tokens[i].isdigit()): 
				val = (val * 10) + int(tokens[i]) 
				i += 1
		elif tokens[i] == ')': 
			while len(ops) != 0 and ops[-1] != '(': 
				val2 = values.pop()
				try: 
					val1 = values.pop()
				except:
					val1=[1,1,1,1]
				op = ops.pop()
				values.append(applyOp(val1, val2, op))
			ops.pop()
		else: 
			while (len(ops) != 0 and
				precedence(ops[-1]) >= precedence(tokens[i])):
				print(values)
				val2 = values.pop()
				try:
					val1 = values.pop() 
				except:
					val1=[1,1,1,1]
				op = ops.pop()
				values.append(applyOp(val1, val2, op))
			if tokens[i]!='#':
				ops.append(tokens[i]) 
		
		i += 1 
	while len(ops) != 0:
		val2 = values.pop() 
		try:
			val1 = values.pop() 
		except:
			val1=[1,1,1,1]
		op = ops.pop()				
		values.append(applyOp(val1, val2, op)) 
	return values[-1]
T=int(input())
mod=998244353
for _ in range(T):
	s=input()
	li=evaluate(s)
	m=sum(li)
	li[0]=(li[0])*power(m,mod-2,mod)%mod
	li[1]=(li[1])*power(m,mod-2,mod)%mod
	li[2]=(li[2])*power(m,mod-2,mod)%mod
	li[3]=(li[3])*power(m,mod-2,mod)%mod
	print(*li)
