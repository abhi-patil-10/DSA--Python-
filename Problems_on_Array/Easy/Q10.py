# Find the missing element in array


# brute force
# arr = [1,2,3,4,5,7]
# n=7

# for i in range(1,n+1):
#     flag = 0
#     for j in range(len(arr)):
#         if arr[j] == i:
#             flag = 1
#             break
    
#     if flag == 0:
#         print(i)

# better approach
# arr = [1,2,3,5,6,7]
# n = len(arr)+1
# hash_arr = [0] * (n+1) 
 
# for i in arr:
#     hash_arr[i] += 1

# for i in range(1,n+1):
#     if hash_arr[i] == 0:
#         print(i)


# optimal approach
arr = [1,2,3,4,6,7]
n = len(arr)+1

sum = n*(n+1)//2
cal_sum = 0
for i in range(len(arr)):
    cal_sum += arr[i]


print(sum-cal_sum)