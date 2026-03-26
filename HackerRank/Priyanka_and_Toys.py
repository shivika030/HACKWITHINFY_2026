def toys(w):
    w.sort()
    m=1
    s=w[0]+4
    for j in range(1,len(w)):
        if w[j] > s:
            m+=1
            s=w[j]+4
    return m        
