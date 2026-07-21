# Find the number is prime or not 
import math
class solution:
    
    def isPrime(self , n):
        if n < 2:
            return False
        count = 0
        
        for i in range(1 , int(math.isqrt(n))+1):
            if n%i==0:
                count += 1
                if i != n//i:
                    count += 1
        
        return count == 2
        
        
sol = solution()
result = sol.isPrime(7)
print(result)
        
    
