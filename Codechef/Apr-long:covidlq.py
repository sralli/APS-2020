for _ in range(int(input())):
    n = int(input())
    arr, k = list(map(int, input().split())), []
    for i in arr:
       
        if i==1:
           
            k.append(arr.index(i)+1)
            arr[arr.index(i)]=0
    flag=0
    for i in k:
        if i+1 in k or i+2 in k or i+3 in k or i+4 in k or i+5 in k:
            flag=1
            break
    if flag==1:
        print("NO")
    else:
        print("YES")
    
