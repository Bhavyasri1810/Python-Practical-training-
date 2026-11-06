def getLCM(a,b):
    start  = max(a,b)

    while True:
        if(start % a ==0 and start % b == 0):  #comparing two multiples
            return start #returns the smallest multiple 
        start += 1 #increments if the number does not divide by a & b
    return -1 #returns false if the if condition is not true

print(getLCM(4,6))

