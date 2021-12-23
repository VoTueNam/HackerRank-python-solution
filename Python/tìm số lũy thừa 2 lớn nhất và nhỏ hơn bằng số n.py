# tìm số lũy thừa 2 lớn nhất và nhỏ hơn bằng số n đã cho
n = 10
if n & (n-1) == 0 and n!=0: #kiểm tra xem n có phải pow của 2 ko
            n /=2
        else:
        	# hàm pow này xác định lũy thừa lớn nhất và bé hơn n
            n -= pow(2,n.bit_length()-1) 
            
