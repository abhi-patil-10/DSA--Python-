# Print all Divisors of a given Number
import math
class solution:
    

    def find_divisors(self, n):
        div_list = []

        for i in range(1,int(math.isqrt(n))+1):
            if n%i == 0:
                div_list.append(i)
                if i != n//i:
                    div_list.append(n//i)


        return div_list


sol = solution()
result = sol.find_divisors(36)
print(result)