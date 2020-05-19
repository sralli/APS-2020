def lcs(s1, s2):
    n = len(s1)
    m = len(s2)
    
    lcs = [[None]*(m+1) for i in range(n+1)]

    for i in range(n+1):
        for j in range(m+1):
            if i==0 or j==0: 
                lcs[i][j]=0
            elif s1[i-1] == s2[j-1]:
                #match
                lcs[i][j] = lcs[i-1][j-1]+1
            else:
            #no match:
                lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

    return lcs[n][m]


print(lcs(input(), input()))