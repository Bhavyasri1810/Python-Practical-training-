#print the nmber of digits in the given number
class Solution:
    def countDigits(self,n: int) -> int:
        #Code here 
        count = 0
        if (n ==0):
            return 1
        else :
          while(n>0):
             n=n//10
             count = count+1
          return count
    countDigits(1,12345)

