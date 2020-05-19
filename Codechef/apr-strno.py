import math
for _ in range(int(input())):
    n , k = map(int, input().split())
    arr = list()
    while(n%2 == 0):
        arr.append(2)
        n= n//2
    
    for i in range(3, math.ceil(math.sqrt(n)), 2): 
        while n % i == 0: 
            n = n / i; 
            arr.append(i) 

    if(n>2):
        arr.append(n)
    print(0 if len(arr)<k else 1)