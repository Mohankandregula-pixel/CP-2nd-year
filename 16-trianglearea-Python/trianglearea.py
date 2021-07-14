# trianglearea(s1, s2, s3)[5pts]
# Write the function trianglearea(s1, s2, s3) that takes 3 floats/ints and returns the area of the
# triangle that has those lengths of its side. If no such triangle exists, return 0. Hint: you
# will probably wish to use Heron's Formula.


import math
def trianglearea(s1, s2, s3):
	# your code goes here
	a = s1
	b = s2
	c = s3
	s =  ((a+b+c)/2)
	area = (s*(s-a)*(s-b)*(s-c))**0.5
	return area

print (trianglearea(4,13,15))
