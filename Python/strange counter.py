# trong giấy đầu value là 3 giảm 1 sau mỗi giây, 
# qua giây thứ 4 thì value sẽ gấp đôi đợt đầu tức là 6 
# và đếm ngược tiếp tục, tương tự về sau

# def strangeCounter(t):
#     n = 3
#     k = n
#     m = 1
#     while True:
#     	if(t==m):
#     		return n 
#     	m +=1
#     	n -=1
#     	if(n==0):
#     		n = k *2
#     		k = n

def strangeCounter(t):
	time = 3
	while True:
		t -= time
		if t <= 0:
			t += time
			return time - t + 1
		time *= 2

# t = 10
# t -time = 7
# time x 2 = 6
# t - time = 1
# time x 2 = 12
# t - time = -11
# t + time = 1
# => 12 - 1 + 1

if __name__ == '__main__':
	t = 21
	print(strangeCounter(t))

