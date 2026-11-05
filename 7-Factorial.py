def getFactorial(n):
   def isPrime(n):
    if(n<2):
        return False 
    for i in range(2,n):
        if(n%i ==0):
            return False
        return True
    fact = 1
    if(n<=1):
        return fact
    for i in range (1,n+1):
        fact = fact * i
    return fact       

getFactorial(5)
