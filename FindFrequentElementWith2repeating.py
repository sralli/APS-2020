def findElement(arr):
  val=0
  for i in range(len(arr)):
    val=val^arr[i]
  return val
A=list(map(int,input().split()))
print(findElement(A))
