# def inRange(low, high, k):
  
#     return low<=k<=high

def getsum(BITTree,i,x): 
    s = 0 #initialize result 
  
    # index in BITree[] is 1 more than the index in arr[] 
    i = i+1
  
    # Traverse ancestors of BITree[index] 
    while i > 0: 
  
        # Add current element of BITree to sum 
        if BITTree[i]-x<0:
            s += BITTree[i] 
  
        # Move index to parent node in getSum View 
        i -= i & (-i) 
    return s 
  
# Updates a node in Binary Index Tree (BITree) at given index 
# in BITree. The given value 'val' is added to BITree[i] and 
# all of its ancestors in tree. 
def updatebit(BITTree , n , i ,v): 
  
    # index in BITree[] is 1 more than the index in arr[] 
    i += 1
  
    # Traverse all ancestors and add 'val' 
    while i <= n: 
  
        # Add 'val' to current node of BI Tree 
        BITTree[i] += v 
  
        # Update index to that of parent in update View 
        i += i & (-i) 
  
  
# Constructs and returns a Binary Indexed Tree for given 
# array of size n. 
def construct(arr, n): 
  
    # Create and initialize BITree[] as 0 
    BITTree = [0]*(n+1) 
  
    # Store the actual values in BITree[] using update() 
    for i in range(n): 
        updatebit(BITTree, n, i, arr[i]) 
  
    # Uncomment below lines to see contents of BITree[] 
    #for i in range(1,n+1): 
    #     print BITTree[i], 
    return BITTree 




for _ in range(int(input())):
    d = {}
    n,m= map(int, input().split())
    arr = list(map(int, input().split()))
    arr.insert(0,0)
    construct(arr,len(arr))
    print()
    while(m):
        c=0
        
        inp = list(map(int, input().split()))
        if repr(inp) in d:
            c+=d[repr(inp)]
        else:
           
            for i in range(inp[0], inp[1]):
                if inRange(min(arr[i], arr[i+1]), max(arr[i], arr[i+1]), inp[2]):
                    c+=1
            d[repr(inp)] = c
            

        
        print(c)
        m-=1



       