def fibonacci(n):
  a=0
  b=1
  c=0
  print(c)
  print(b)
  for i in range(n-2):
    c=a+b
    a=b
    b=c
    print(c)
n=int(input())
fibonacci(n)
