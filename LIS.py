def LIS(arr):
    dp = [1*len(arr)]

    for i in range(len(arr)):
        for j in range(i):
            if arr[i]>arr[j] and dp[j]>dp[i-1]:
                dp[i]=dp[j+1]
    return max(dp)

arr = list(map(int, input().split()))
print(LIS(arr))