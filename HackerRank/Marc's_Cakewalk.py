def marcsCakewalk(calorie):
    calorie.sort()
    calorie.reverse()
    sum=0
    for i in range(len(calorie)):
        sum+=(2**i) * (calorie[i])
    return sum 
