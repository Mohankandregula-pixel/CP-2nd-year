def isPrime(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                return False
        return True
def revNumber(n):
    p=n
    rn = 0
    while(n!=0):
        rm = n%10
        rn = rn*10 + rm
        n = n//10
    return (rn==p)

def isPalindromePrime(n):
    if (isPrime(n)==True) and (revNumber(n)==True):
        return True
    return False


print(isPalindromePrime(131))