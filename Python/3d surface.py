def surfaceArea(A):
	#2 surface
	summ = len(A)*len(A[0])*2
	dong = 0
	tay = 0
	bac = 0
	nam = 0

	for x in range(len(A)):
		tay += A[x][0]
		dong += A[x][len(A[0])-1]
	for y in range(len(A[0])):
		bac += A[0][y]
		nam += A[len(A)-1][y]

	#chenh lenh 2 o lien tiep
	cl = 0
	for x in range(len(A)):
		for y in range(len(A[0])-1):
			if(A[x][y] != A[x][y+1]):
				cl += abs(A[x][y]-A[x][y+1])
			
	for x in range(len(A)-1):
		for y in range(len(A[0])):
			if(A[x][y] != A[x+1][y]):
				cl += abs(A[x][y]-A[x+1][y])

	return summ + bac + nam + tay + dong + cl


a = [[1,3,4],[2,2,3],[1,2,4]]

b = [[1,2],[1,1]]

#print(b[0][1], b[1][1])
print(surfaceArea(a))