def substrings(n):
	s=n[::-1]
	listOfString=list(s)
	count=0
	for j in range(len(s)):
		s1=s[j:]
		val=1
		for i in range(len(s1)):
			count+=(int(s1[i]))*(len(s1)-i)*val
			val*=10
	return count
n=input()
print(substrings(n))
