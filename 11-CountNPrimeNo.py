def isPrime(n):    #to check for the prime numbers
    if(n<2):
        return False
    for i in range(2,n):
        if(n%i==0):
            return False
        return True
    
def CountPrime(num):      #to count the prime numbers
    num = 10
    count = 0
    for i in range(1,num+1):          #calling isPrime
        if(isPrime(i)):
            count+=1
    return count
print(CountPrime(10))

     

