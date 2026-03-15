def climbingLeaderboard(ranked, player):
    ranked = list(dict.fromkeys(ranked))
    arr=[]
    i=len(ranked)-1
    for j in player:
        while i>=0 and j>=ranked[i]:
            i-=1
        arr.append(i+2)    
    return arr      
