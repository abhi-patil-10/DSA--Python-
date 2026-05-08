#Q.1 - Print sum of n numbers 
# ex : n=3
# 1+2+3 = 6

#using parameterized
# def sum(n,sum):
#     if n < 1:
#         print(sum)
#         return
    
#     sum = sum + n
#     sum(n-1,sum)
    
# print(sum(3,0))


#using functional recursion
# def sum(n):
#     if n == 0:
#         return 0
    
#     return n + sum(n-1)

# print(sum(3))
    
    
# Q.2 - find the factorial of n
# ex : 4
# 1 * 2 * 3 * 4 = 24

def fact(n):
    if n == 1:
        return 1
    
    return n * fact(n-1)

print(fact(4))