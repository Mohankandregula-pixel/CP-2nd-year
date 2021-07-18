# Write the function getKthDigit(n, k) that takes 
# a possibly-negative int n and a non-negative int k, 
# and returns the kth digit of n, starting from 0, counting from the right.
# if the kth digit is not present return 0 



def fun_get_kth_digit(digit, k):
	digit = abs(digit) 
	a = digit//100
	b = (digit//10)%10
	c = digit%10
	list = [a,b,c]
	m = list[::-1]
	if k == abs(k) and k < len(m):
		return m[k]
	else:
		return 0

print(fun_get_kth_digit(789,2))