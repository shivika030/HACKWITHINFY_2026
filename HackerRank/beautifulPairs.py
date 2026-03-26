def beautifulPairs(A, B):
    freq={}
    match=0
    
    for i in A:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
            
    for i in B:
        if i in freq and freq[i]>0:
            match+=1
            freq[i]-=1
            
    if match < len(A):
        return match + 1
    else:
        return match - 1
