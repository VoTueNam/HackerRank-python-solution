def maxCost(cost, labels, dailyCount):
    n = 0
    maxx = 0
    countday = 0
    illegal = 0
    for i in range(len(cost)):
        n += cost[i]
        if maxx < n:
            maxx = n
        if labels[i] =="legal":
            countday +=1
        # if countday == 0:
        #     n = 0
        if countday == dailyCount:
            countday = 0
            n = 0
            illegal = 1
    if illegal == 0:
        return 0
    else:
        return maxx

if __name__ == '__main__':
    

    cost = [0,3,2,3,4]
    labels = ["legal","legal","illegal","legal","legal"]
    dailyCount = 1

    result = maxCost(cost, labels, dailyCount)

    print(result)