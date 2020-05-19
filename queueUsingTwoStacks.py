q=int(input())
l=[]
for _ in range(q):
    A=list(map(int,input().split()))
    if A[0]==1:
        l.append(A[1])
    elif A[0]==2:
        l.pop(0)
    else:
        print(l[0])
