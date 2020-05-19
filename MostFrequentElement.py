def maxFrequentElement(arr):
  return max(set(arr),key=arr.count)
A=list(map(int,input().split()))
print(maxFrequentElement(A))
