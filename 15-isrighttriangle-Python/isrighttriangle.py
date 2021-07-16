# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.

def isrighttriangle(x1, y1, x2, y2, x3, y3):
	# your code goes here
	# x1 = abs(x1)
	# x2 = abs(x2)
	# x3 = abs(x3)
	# y1 = abs(y1)
	# y2 = abs(y2)
	# y3 = abs(y3)
	a = ((x2-x1)**2 + (y2-y1)**2)*0.5
	b = ((x3-x2)**2 + (y3-y2)**2)*0.5
	c = ((x3-x1)**2 + (y3-y1)**2)*0.5
	# if (a**2+b**2)==c**2 or (b**2+c**2)==a**2 or (a**2+c**2)==b**2 :
	if (a>0 and b>0 and c>0) and ((a+b)==c or (b+c)==a or (a+c)==b):	
		return True
	else:
		return False

print(isrighttriangle(13, -1, -9, 3, -3, -9))
