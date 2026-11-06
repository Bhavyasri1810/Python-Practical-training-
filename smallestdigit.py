def getsmallestDigit(n):
    small_digit = 10
    while(n>0):
        current_digit  = n % 10
        if(small_digit > current_digit):
            small_digit = current_digit
        n = n//10
    return small_digit
n = int(input("Enter a number:"))
print(getsmallestDigit(n))