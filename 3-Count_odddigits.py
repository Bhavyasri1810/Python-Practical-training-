def count_odd_digits(n):
    odd_count = 0
    if n == 0:
        print(odd_count)
        return 1 
    while n > 0:
        rem = n % 10
        if rem % 2 != 0:
            odd_count = odd_count + 1
        n = n // 10
        
    print(odd_count)

count_odd_digits(1234567)
