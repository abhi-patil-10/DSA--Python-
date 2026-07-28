

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


# nums = list(input().split(" "))
# substring = input()
# counter = 0

# for word in nums:
#     if word == substring:
#         counter += 1

# print(counter)

    

# print(nums)

# class Solution(object):
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         i=0
#         for j in range(1,len(nums)):
#             if nums[i] != nums[j]:
#                 nums[i+1] = nums[j]
#                 i += 1
#         print(i+1)
#         return nums[:i+1]

# sol = Solution()
# nums = [1,1,1,2,2,2,3,4,4,5]
# print(sol.removeDuplicates(nums))

# def rotate(nums,k):
#     temp = []
#     for j in range(k+1):
#         temp.append(nums[j])
        
#     for i in range(k+1,len(nums)):
#         nums[i-(k+1)] =nums[i]
    
#     for x in range(len(nums)-(k+1),len(nums)):
#         nums[x] = temp[x-(len(nums)-k-1)]
        
#     return nums

# nums = [1,2,3,4,5,6,7]
# k = 3
# print(rotate(nums,k))

# s='HackerRank.com presents "Pythonist 2".'
# temp = []
# sample = ""
# # print(ord('A'))   
# for i in range(len(s)):
#     if s[i].isupper():
#         temp.append(s[i].lower())
#     elif s[i].islower():
#         temp.append(s[i].upper())
#     else:
#         temp.append(s[i])

# # print(temp)

#     # sample = "".join(x)
# ans = "".join(temp)
# print(ans)
# line = "this is a string"   

# ans = line.split(" ")
# print("-".join(ans))


# if __name__ == '__main__':
#     s = "qA2"
#     alphanum = False
#     alpha = False
#     digit = False
#     lower = False
#     upper = False
#     temp = []
    
#     for i in s:
#         if i.isalnum():
#             alphanum = True
#     for i in s:
#         if i.isalpha():
#             alpha = True
#     for i in s:
#         if i.isdigit():
#             digit = True
        
#     for i in s:
#         if i.islower():
#             lower = True 
    
#     for i in s:
#         if i.isupper():
#             upper = True
    
   
        
#     print(alphanum)
#     print(alpha)
#     print(digit)
#     print(lower)
#     print(upper)

# string = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
# max_width = 4
# result = ""
# for i in range(0,len(string),max_width):
#     result += string[i:i+max_width] + "\n"
    
# # for i in range(1,26,4):
# #     print(i)
# print(result)


for i in 