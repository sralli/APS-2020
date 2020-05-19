def caesarCipher(s, k):
	s1=""
	k=k%26
	for i in range(0,len(s)):
		n=k
		if s[i].isalpha():
			if ord(s[i])+k > 122 and ord(s[i])>=97 and ord(s[i])<=122:
				val=97
				n=k-(122-ord(s[i]))-1
			elif ord(s[i])+k > 90 and ord(s[i])>=65 and ord(s[i])<=90:
				val=65
				n=k-(90-ord(s[i]))-1
			else:
				val=ord(s[i])
			s1+=chr(val+n)  
		else:
			s1+=s[i]
	return(s1)
s=input()
k=int(input())
print(caesarCipher(s,k))
