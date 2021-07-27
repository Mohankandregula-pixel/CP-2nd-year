# Write the function nth_happy_number(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:

# https://en.wikipedia.org/wiki/Happy_number#:~:text=In%20number%20theory%2C%20a%20happy,starting%20with%20and%20eventually%20reaches
# Read more about the happy number from the above link.

# assert(nth_happy_number(1) == 1)
# assert(nth_happy_number(2) == 7)
# assert(nth_happy_number(3) == 10)
# assert(nth_happy_number(4) == 13)
# assert(nth_happy_number(5) == 19)
# assert(nth_happy_number(6) == 23)
# assert(nth_happy_number(7) == 28)
# assert(nth_happy_number(8) == 31)

def squareSumNumber(n):
    sum1 = 0
    while (n > 0):
        sum1 += (n%10)**2
        n = n//10
    return sum1
        

def isHappyNumber(n):
    set1 = {-1}
    while True:
        n = squareSumNumber(n)
        if n == 1:
            return True
        if n in set1:
            return False
        else:
            set1.add(n)
    
    
def nth_happy_number(n):
	count = 0
	num = 1
	while (count != n):
		if isHappyNumber(num):
			count += 1
		num = num + 1
	return num - 1

print(nth_happy_number(4))
  
