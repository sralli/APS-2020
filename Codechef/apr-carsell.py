def dec(arr):
    for i in range(len(arr)):
        arr[i] = arr[i]-1
        if arr[i]<0:
            arr[i]=0
    return arr
        


for _ in range(int(input())):
    n = int(input())
    arr = sorted(list(map(int, input().split())), reverse=True)
    su = 0
    for i in range(len(arr)):
       
        if arr[i]-i<=0:
            su+=0
        else:
            su+=arr[i]-i

    print(su%1000000007)