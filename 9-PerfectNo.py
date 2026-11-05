def isPerfectNumber(n):
    sum = 0
    for i in range(1,n):
        if(n % i == 0):
            sum =+ i
    return sum == n
if (isPerfectNumber(6)):
    print("Perfect Number")
else:
    print("Not a Perfect number")

isPerfectNumber(6)

