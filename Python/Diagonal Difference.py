ar3 = [ [1,2,3], [1,1,6], [7,8,9] ]

x1 = 0
x2 = 0


for i in range(len(ar3)):
	for y in range(len(ar3[0])):
		if(i == y):
			x1 += ar3[i][y]
			
		if(i+y)==(len(ar3)-1):
			x2 += ar3[i][y]
#print(f"x1 = {x1} \nx2 = {x2}")