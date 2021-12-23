def flippingMatrix(matrix):
    a = matrix
    suma = 0
    n = int(len(matrix)/2)
    for i in range(n):
        for j in range(n):
            suma += max(max(a[i][j],a[2*n-i-1][j]),max(a[i][2*n-j-1],a[2*n-i-1][2*n-j-1]))
    return suma

e = [[112,42,83,119],[56,125,56,49],[15,78,101,43],[62,98,114,108]]

print(flippingMatrix(e))