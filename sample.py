

# def subset(A,B):
#     counter = 0
#     for i in A:
#         if i in B:
#             counter += 1
        
#     if counter == len(A):
#         return True
#     else:
#         return False
        
    
# # A = set(map(int,input().split()))
# # B = set(map(int,input().split()))
# # print(A.issubset(B))

# # 1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
# # 2
# # 1 2 3 4 5
# # 100 11 12
# # A = (1,2,3,4,5,6,7,8,9,10,11,12,23,45,84,78)
# # B = (1,2,3,4,5)
# # C = (100, 11, 12)
# # A = set(map(int,input().split()))
# # no_of_set = int(input())
# # for _ in range(no_of_set):
# #     B = set(map(int,input().split()))
# #     C = set(map(int,input().split()))
# #     if A.issuperset(B) and A.issuperset(C):
# #         return True
# #     else:
# #         return False

# no_of_testcases = int(input())
# for _ in range(no_of_testcases):
#     A,B = input().split()
#     if not A.isdigit():
#         non_int = A
#     else:
#         non_int = B
    
#     try:
#         print(int(A)//int(B))
#     except ZeroDivisionError:
#         print("Error Code: integer division or modulo by zero")
#     except ValueError:
#         print("Error Code: invalid literal for int() with base 10: '{}'"
#         .format(non_int))


arr = list(input().split(" "))
substring = input()
counter = 0

for word in arr:
    if word == substring:
        counter += 1

print(counter)

    

# print(arr)