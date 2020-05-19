from collections import defaultdict

for _ in range(int(input())):
    d = defaultdict(int)
    n,m = map(int, input().split())
    ids = list(map(int, input().split()))
    prices = list(map(int, input().split()))
    for i, j in zip(ids, prices):
        d[i]+=j
    print(min(d.values()))
    
