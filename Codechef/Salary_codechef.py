for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split(' ')))
    
    count = 0
    sm = sum(arr)
    small = min(arr)
    num = sm -(n*small)
    print(num)