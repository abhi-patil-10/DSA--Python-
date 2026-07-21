# All problems solved by recursion

# Q.1 - print names 5 times

# def recursion_function(name,n):
#     if n < 1:
#         return
#     print(name)k
#     recursion_function(name,n-1)

# print(recursion_function("Abhijeet",5))

# Q.2 - print linearly from n to 1

# def recursion_function(n):
#     if n == 0:
#         return
#     print(n)
#     recursion_function(n-1)

# print(recursion_function(10))

# Q.3 - print linearly from 1 to n

# def recursion_function(s,n):
#     if s == n+1:
#         return
#     print(s)
#     recursion_function(s+1,n)
    
# print(recursion_function(1,10))

# Q.4 - print linearly from 1 to n(use backtracking)
# [you should not used increment like s+1]

# def recursion_function(n):
#     if n == 0:
#         return
    
#     recursion_function(n-1)
#     print(n)

# print(recursion_function(10))
# Q.5 - print linearly from n to 1(use backtracking)
# [you should not used increment like s-1]

def recursion_function(s,n):
    if s > n:
        return
    
    recursion_function(s+1,n)
    print(s)

print(recursion_function(1,10))