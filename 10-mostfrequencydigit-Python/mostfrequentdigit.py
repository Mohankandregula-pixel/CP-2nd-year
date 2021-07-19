# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
	# your code goes here
	res = list(map(int, str(n)))
	print (res)
	counter = 0
	num = res[0]
	for i in res:
		curr_frequency = res.count(i)
		if(curr_frequency > counter):
			counter = curr_frequency
			num = i
		elif curr_frequency == counter and (i < num):
			num = i
	return num
 
print(mostfrequentdigit(5231123123123))
