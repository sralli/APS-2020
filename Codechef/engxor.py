from sys import stdin, stdout 


def Parity(n): 
    global even
    global odd
    global f
    parity = 0
    while n: 
        parity = ~parity 
        n = n & (n - 1) 
    
    if f!=0: 
        if parity:
            even+=1
        else:
            odd+=1
    else:
        return parity
  
  
for _ in range(int(input())):
    even, odd = 0,0
    n,q = map(int, input().split())
    f=1
    arr = list(map(Parity, map(int, stdin.readline().split())))
    f = 0
    for i in range(q):
         if Parity(int(input())):
            print(even, odd)
         else:
            print(odd, even)
