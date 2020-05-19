from random import seed, randint

seed(7)

for _ in range(int(input())):
    n,m,k = map(int, input().split(' '))
    for i in range(n):
        inp = list(map(int, input().split()))
    
    print(*[randint(1,m) for i in range(n)])
        
    
