arr = [[1,1,1,0,0,0],[0,1,0,0,0,0],[1,1,1,0,0,0],[1,1,2,4,4,0],[0,0,0,0,2,0],[0,0,1,2,4,0]]

ar = [[1,2,3],[4,5,6],[7,8,9]]

def hourglass(n,m,ar):
    summ = 0
    for i in range(n,n+3):
        for y in range(m,m+3):
            summ += ar[i][y]
            print(f"ar[{i}][{y}]=",ar[i][y], end =" ")
        print(" ") 
    
    print(summ)
    print(f"ar[{n+1}][{m}]=",ar[m+1][n], f"ar[{n+1}][{m+2}]=",ar[m+1][n+2])
    summ = summ - ar[n+1][m] - ar[n+1][m+2]
    print(summ)
    return summ

def hourglassSum(arr):
    ac = []
    for i in range(len(arr)-2):
        for y in range(len(arr[i])-2):
            ac.append(hourglass(i,y,arr))
    summ = max(ac)
    return summ

hourglass(0,1,arr)