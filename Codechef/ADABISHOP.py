for _ in range(int(input())):
    arr = [list(i) for i in "11 44 17  28  82  71  53  31  13  68  86  75  84  51  15  48  66  88".split()]
    inp = list(input().split())
    arr1=[]
    if inp!=['1', '1'] and len(set(inp))==2:
        inp = [str((int(inp[0])+int(inp[1]))//2),str((int(inp[0])+int(inp[1]))//2)]  
        arr1.append(inp)
        inp = ['1', '1']
        arr1.append(inp)
    elif inp!=['1', '1'] and len(set(inp))==1:
        inp = ['1', '1']
        arr1.append(inp)

    
    

    if inp in arr:
        del arr[0]
        [arr1.append(i) for i in arr]
    
    print(len(arr1))
    for i in arr1:
        print(i[0], i[1])
    
    #inp =  list(map(int, input().split()))
