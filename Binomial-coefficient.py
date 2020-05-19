#1 Two-Dim Array:

def two_dim(n,k):
    c = [[0]*(k+1) for i in range(n+1)]
    for i in range(n+1):
        for j in range(0, min(i,k)+1):
            if j==0 or j==i:
                c[i][j] = 1
            else: 
                c[i][j] = c[i-1][j]+c[i-1][j-1]
            
    return c[n][k]

print(two_dim(4,2))



# recursive func:

def rec_bin(n,k):
    if n==k or k==0:
         return 1
    else:
        return rec_bin(n-1,k-1) + rec_bin(n-1,k)
    
print(rec_bin(5,2))


# 1-d array:

def one_dim(n,k):
    c = [0]*(n+1)
    c[0] = 1
    for i in range(1,n+1):
        j = min(i,k)
        while(j>0):
            c[j] = c[j] + c[j-1]
            j-=1
    return c[k]

print(one_dim(4,2))

     


