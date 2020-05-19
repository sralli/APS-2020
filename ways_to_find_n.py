
def subset_sum(numbers, target, partial=[], partial_sum=0):
    if partial_sum == target:
        yield partial
    if partial_sum >= target:
        return 0
    for index, num in enumerate(numbers):
        remaining = numbers[index + 0:]
        yield from subset_sum(remaining, target, partial + [num], partial_sum + num)





def ways(n, num1, num2, num3):
    dp = bytearray(n+1)
    dp[0] = 1
    for i in range(num1, n+1):
        if dp[i-num1] != 0:
            dp[i]+=dp[i-num1]
    for i in range(num2, n+1):
        if dp[i-num2] != 0:
            dp[i]+=dp[i-num2]
    for i in range(num3, n+1):
        if dp[i-num3] != 0:
            dp[i]+=dp[i-num3] 

    return dp[n]


print(ways(13,3,5,10))
for i in subset_sum([3,5,10], 15):
    print(i)