# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 



def fun_set_kth_digit(n, k, d):
	if n>0:
		if k>=3:
			m = str(n)
			k = int (f"{d}{m}")
			return k

				
		a = n//100
		b = (n//10)%10
		c = n%10
		m = [a,b,c]
		m.reverse()
		m[k]=d
		m.reverse()
		n = str(m[0])
		n += str (m[1])
		n += str (m[2])
		return int(n)
	if n<0:
		n=abs(n)
		if k>=3:
			m = str(n)
			k = int(f"{d}{m}")
			return -k

		
		a = n//100
		b = (n//10)%10
		c = n%10
		m = [a,b,c]
		m.reverse()
		m[k]=d
		m.reverse()
		n = str(m[0])
		n += str (m[1])
		n += str (m[2])

		return int(-n)	


print(fun_set_kth_digit(-468, 3, 1))

	# if len(str(n))>=k:
	# 	a = n//100
	# 	b = (n//10)%10
	# 	c = n%10
	# 	m = [a,b,c]
	# 	m[k]=d
	# 	n = str(m[0])
	# 	n += str (m[1])
	# 	n += str (m[2])
		
	# elif len(str(n))<k:
	# 	a = n//100
	# 	b = (n//10)%10
	# 	c = n%10
	# 	m = [a,b,c]
	# 	m[-k]=d
	# 	n = str(m[0])
	# 	n += str (m[1])
	# 	n += str (m[2])
	# 	n += str (m[-k])