#to print the Armstrong Number :
def isArmstrongNumber(n):
    count = 0
    temp = n
    sum = 0
    count = len(str("n"))
    while(temp > 0):
        current_digit = temp % 10
        sum += current_digit ** count
        temp = temp // 10

    if (sum ==  n):
        print("Armstrong number")
    else :
        print("Not an armstrong")
    
isArmstrongNumber(371)


    