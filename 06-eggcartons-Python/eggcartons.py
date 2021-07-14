# Write the function eggCartons(eggs) that takes 
# a non-negative integer number of eggs, and returns 
# the smallest integer number of cartons required to hold 
# that many eggs, where a carton may hold up to 12 eggs


def fun_eggcartons(eggs):
	# your code goes here
	m = eggs//12
	if eggs == 0 or eggs == 1:
		return 0
	elif eggs%12 != 0:
		m += 1
	return m
print(fun_eggcartons(23))
