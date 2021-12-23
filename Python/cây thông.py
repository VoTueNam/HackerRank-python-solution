n = 3
m = n-1
for i in range(n):
	print("")
	for y in range(n):
		if y < m:
			print(" ", end = '')
		if(y >= m):
			print("#", end = '')
	m -=1

# def staircase(num_stairs):
#     for stairs in range(1, num_stairs + 1):
#         print(' ' * (num_stairs - stairs) + '#' * stairs)
# staircase(12)