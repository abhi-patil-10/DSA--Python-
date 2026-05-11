# All problems solved by recursion

# Q.1 - print names 5 times



def recursion_function(n):
    
    if n < 1:      
        return
    
    print("abhijeet")
    recursion_function(n-1)
    
print(recursion_function(10))


# Q.2 - print linearly from n to 1


# def recursion_function(n):
    
#     if n ==0:
#         return 
#     print(n)
#    #n -= 1
#     recursion_function(n-1)
    
# print(recursion_function(20))


# Q.3 - print linearly from 1 to n


# def recursion_function(s,n):
    
#     if s == n+1:
#         return
#     print(s)
#   # s += 1
#     recursion_function(s+1,n)

# print(recursion_function(1,25))


# Q.4 - print linearly from 1 to n(use backtracking)
# [you should not used increment like s+1]

# def recursion_function(i,n):
#     if i < 1:
#         return
    
#     recursion_function(i-1 , n)
#     print(i)

# print(recursion_function(4,4))


# Q.5 - print linearly from n to 1(use backtracking)
# [you should not used increment like s-1]

def recursion_function(i,n):
    if i > n:
        return
    
    recursion_function(i+1,n)
    print(i)

print(recursion_function(1,5))