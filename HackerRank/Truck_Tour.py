def truckTour(petrolpumps):
    tank=0
    start=0
    total=0
    
    for i in range(len(petrolpumps)):
        petrol=petrolpumps[i][0]
        dist=petrolpumps[i][1]
        
        diff=petrol-dist
        tank+=diff
        total+=diff
        
        if tank <0:
            start=i+1
            tank=0
            
    return start if total>=0 else -1 
