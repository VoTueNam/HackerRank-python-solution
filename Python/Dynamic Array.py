def idx(x, last, n):
    return (x^last)%n

def dynamicArray(n, queries):
    arr = [[] for i in range(n)]
    # arr = [None,None]
    # arr[0] = []
    # arr[1] = []
    last = []
    las = 0
    for i in queries:
        idxx = idx(i[1],las,n)
        if(i[0]==1):
            arr[idxx].append(i[2])
        if(i[0]==2):
            las = arr[idxx][i[2]%len(arr[idxx])]
            last.append(las)
    
    return last


n = 2
queries = [[1,0,5],[1,1,7],[1,0,3],[2,1,0],[2,1,1]]
result = dynamicArray(n, queries)
print(result)