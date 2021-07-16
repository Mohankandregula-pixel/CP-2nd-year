# Write the function pascalsTriangleValue(row, col) 
# that takes int values row and col, and returns the 
# value in the given row and column of Pascal's 
# Triangle where the triangle starts at row 0, and 
# each row starts at column 0. If either row or col 
# are not legal values, return None, instead of crashing. 


def factorial(n):
	b = 1
	for a in range(1,n+1):
		b=b*a
	return b


def fun_pascaltrianglevalue(row, col):
	a = factorial(row)/(factorial(col)*(factorial(row-col)))
	return int(a)