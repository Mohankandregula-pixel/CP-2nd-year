# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
	# your code goes here
	n = abs(n)
	if n<100:
		return False
	res = list(map(int, str(n)))
	# sorted_list = sorted(res)

	# range_list=list(range(min(res), max(res)+1))
	count = 0
	m = 0
	for i in res:
		if (i == res[m]):
			count += 1
			m += 1
	if n <= 10:
		return False
	elif count == 0 and n//10 == n%10:
		return True
	elif count > 1 :
		return True 
	else:
		return False

print(hasconsecutivedigits(-24))