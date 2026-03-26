def luckBalance(k, c):
    mini=[]
    sums=0
    for i in range(len(c)):
        if c[i][-1]==0:
            sums+=c[i][0]
        else:
            sums+=c[i][0]
            mini.append(c[i][0])
    mini.sort()  
    for i in range(len(mini)-k):
        sums-=mini[i]*2
    return sums  
