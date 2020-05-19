def pangrams(s):
    flag=0
    s=s.lower()
    print(s)
    for i in "abcdefghijklmnopqrstuvwxyz":
        if i not in s:
            print(i)
            flag=1
            return("not pangram")
    if flag==0:
        return("pangram")
val=input()
print(pangrams(val))
