#lấy n số nguyên đầu tiên (i) trị tuyệt đối trừ cho k,
#nếu kết quả >0 thì ra
#<=0 thì đổi dấu trừ thành cộng: i + k
#nếu số ghi ra bị trùng với số trước đó thì cũng trừ thành cộng
# def absolutePermutation(n, k):
# 	arr = []
# 	ac = []
# 	for i in range(1,n+1):
# 		if i - k > 0:
# 			if i - k not in ac:
# 				ac.append(i - k)
# 			else:
# 				ac.append(i + k)
# 				if i + k > n:
# 					return [-1]
# 		if i - k <= 0:
# 			ac.append(i + k)
# 			if i + k > n:
# 				return [-1]
# 	return ac


def asbPer(n,k):
	if k == 0:
		return [i for i in range(1,n+1)]

	elif n%(2*k): 
		return [-1]
	
	else:
		res = [None] * (n+1)
		for i in range(1, n+1):
			if res[i] is None:
				res[i] = i + k
				res[i + k] = i

		return res[1:]



n = [2,1]
k = [1,2]


for i in range(len(n)):
	# m = absolutePermutation(n[i],k[i])
	m = asbPer(n[i],k[i])
	print(m)
