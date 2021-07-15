# removeDuplicate(text) [10 pts]
# Write a program to remove all the duplicate characters from a given input String,e.g.
# if given String is "JavaPython" then the output should be "JavPython".
# The second or further occurrence of duplicate should be removed.
from collections import OrderedDict 
def removeduplicate(text):
	# Your code goes here
	# n = list(text)
	# m = ""
	# output=""
	# for i in range(len(n)):
	# 	m += n[i]

	# return set(m)
	return "".join(OrderedDict.fromkeys(text))

print(removeduplicate("Helloworld"))