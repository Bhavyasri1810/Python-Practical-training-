def getGCD(a,b):
    mini_value = min(a,b)
    ans = 0
    for i in range(1,mini_value):
        if(a % i == 0 and b % i == 0):
            ans  = i
    return ans
a = 12
b = 24
print(getGCD(12,24))
  
         