def getPrimeNumber(n):
    if(n<2):
        return False
    count = 0
    for i in range (1,n+1):
        if(n% i == 0):
            count += 1
    if(count ==2):
        return True
    return False

n  = int(input("Enter a number :"))
if(getPrimeNumber(n)==True):
    print("It is Prime number")
else:
    print("It is not a Prime number")
    



