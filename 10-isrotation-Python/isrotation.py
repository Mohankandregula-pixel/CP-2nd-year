# isRotation(x, y) [15 pts]
# Write the function isRotation(x, y) that takes two non-negative integers x and y, both 
# guaranteed to not contain any 0's, and 
# returns True if x is a rotation of the digits of y and False otherwise. For example, 
# 3412 is a rotation of 1234. Any number 
# is a rotation of itself.

# def isrotation(x, y):
#     y=y%len(x)
#     rotated= x[y:] + x[:y]
#     return rotated

def readArray():
    a = []
    l = int(input())
    for i in range(l):
        a.append(int(input()))
    return a

def isRotation(a,b):
    if (len(a)!=len(b)):
        return False
    l=len(b)
    temp=[]
    temp= temp + b[l-2:] + b[0: l-2]
    return (a == temp)
        
#a=[5,2,3,4,5,6]  b=[5,3,4,5,2,6] #2
#a=[5,2,3,4,5,6]  b=[5,4,5,6,2,3] #1


print(isRotation(readArray(),readArray()))





