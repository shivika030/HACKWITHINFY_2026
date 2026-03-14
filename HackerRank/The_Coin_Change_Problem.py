def getWays(n, c):
    m=len(c)
    a=[[0]*(n+1) for _ in range(m+1)]
    
    for i in range(m+1):
        a[i][0]=1
    for i in range (1,m+1):
        for j in range(1,n+1):
            
            if c[i-1]>j:
                a[i][j]= a[i-1][j]
            else:
                a[i][j]= a[i-1][j]+a[i][j-c[i-1]]
    return a[m][n]            
