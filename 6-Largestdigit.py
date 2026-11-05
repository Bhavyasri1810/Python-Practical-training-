#to print the largest number 
def getLargestDigit(n):
    largest_digit = -1
    while(n>0):
        current_digit  = n % 10
        if(largest_digit < current_digit):
            largest_digit = current_digit
        n = n//10
    return largest_digit
n = int(input("Enter a number:"))
print(getLargestDigit(n))
