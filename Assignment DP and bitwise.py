import sys
def assignment(cost,n):
    dp = [sys.maxsize for i in range(2**n)]
    dp[0] = 0
    for mask in range(0,2**n):
        x = bin(mask).count('1')
        for j in range(0, n):
          
            if (mask& 1<<j )==0:
                dp[mask | 1<<j] = min(dp[mask| 1<<j], dp[mask]+cost[x][j])
    return (dp)


n=3
cost = [[3,2,7],[5,1,3],[2,7,2]]
print(assignment(cost, n))