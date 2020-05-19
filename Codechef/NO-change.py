def fun(arr, k):
    dp = [0 for i in range(len(arr))]
    num = len(arr)-1
    while k>0 and num>=0:
        if k%arr[num]==0:
            dp[num] = (k//arr[num])-1
            k = k-((k//arr[num]-1)*arr[num])
        else:
            dp[num] = (k//arr[num])+1
            k = k-((k//arr[num]+1)*arr[num])
        num-=1
    print("YES", *dp)



for _ in range(int(input())):
    n,k = map(int, input().split(' '))
    arr = list(map(int, input().split(' ')))
    c,f = 0, []
    for i in arr:
        if k%i!=0:
            c=1
            break
    for i in range(n-1):
        for j in range(i, n):
            if arr[j]%arr[i]!=0:
                c=1
                break
    if c==0:
        print("NO")
    else:
        fun(arr,k)
        
