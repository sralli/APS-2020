def Solve (N):
    count=1
    i=2
    while(i*i<=N):
        if N%i==0:
            count=count+i+(N//i)
        i+=1
    if count==N and N!=1:
        return "YES"
    else:
        return "NO"
T = int(input())
for _ in range(T):
    N = int(input())
    out = Solve(N)
    print (out)
