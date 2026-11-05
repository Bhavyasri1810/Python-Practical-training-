def is_palindrome(n):
    original = n
    reverse = 0
    while (n > 0):
        remainder = n % 10
        reverse = (reverse * 10) + remainder
        n = n // 10
    if (original == reverse):
        print("is a palindrome") 
    else:
        print("Not a palindrome ") 

is_palindrome(12321)
