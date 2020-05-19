def subset_sum(arr, sum1, n):
    dp = [[0 for i in range(0, sum1+1)] for j in range(0, n+1)]
    
    for i in range(n+1):
        dp[i][0] = 1
    
    for j in range(1,sum1+1):
        dp[0][j] = 0
    
    for i in range(1, n+1):
        for j in range(1, sum1+1):
            if dp[i-1][j]==1:
                dp[i][j]=1
            else:
                if arr[i-1]>j:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j-arr[i-1]]
    print(dp)


subset_sum([1,2,3,5,7], 9, 5)