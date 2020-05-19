def solve(n):
    if n==1:
        print(1)
        print(*[1,1])
    elif n%2==0:
        print(int(n/2))
        for k in range(1,n+1,2):
            print(*[2,k,k+1])
    else:
        print(n//2)
        print(*[3,1,2,n])
        for i in range(3,n,2):
            print(*[2,i,i+1])

   

for t in range(int(input())):
    n = int(input())
    solve(n)