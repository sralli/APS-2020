t,s = map(int, input().split())
for i in range(t):
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    arr2 = sorted(list(map(int, input().split())))
  
    flag=0
    for i,j in zip(arr,arr2):
        if j<=i:
            print("N0")
            flag=1
            break
    if flag==0:
        print("YES")

