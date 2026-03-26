def maximumPerimeterTriangle(s):
    s.sort()
    for i in range(len(s)-3,-1,-1):
        if s[i]+s[i+1]>s[i+2]:
            return [s[i],s[i+1],s[i+2]]  
    return [-1]
