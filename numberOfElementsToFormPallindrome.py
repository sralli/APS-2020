flag=0
val=[]
for i in range(999,99,-1):
	for j in range(999,99,-1):
		num=i*j
		num=str(num)
		if len(num)==6:
			if num[0]==num[5] and num[1]==num[4] and num[2]==num[3]:
				val.append(int(num))
		elif len(num)==5:
			if num[0]==num[4] and num[1]==num[3]:
				val.append(int(num))
print(val)
print(max(val))
